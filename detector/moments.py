import cv2
import numpy as np
def get_action(image):
    lower_bound = np.array([150,100,250])
    upper_bound = np.array([150,100,250])
    mask = cv2.inRange(image, lower_bound, upper_bound)
    #mask = cv2.bitwise_and(image, image, mask=mask)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print('Не видно контуров')
        return [0]

    cnt = max(contours, key=cv2.contourArea)

    
    moments = cv2.moments(cnt)


    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
    else:
        cx, cy = None, None
    print(f'cx = {cx} \t cy = {cy}')
    return [cx, cy]




def get_contour_equation(image):
    lower_bound = np.array([150,100,250])
    upper_bound = np.array([150,100,250])
    mask = cv2.inRange(image, lower_bound, upper_bound)
    #mask = cv2.bitwise_and(image, image, mask=mask)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print('Не видно контуров')
        return [0]

    cnt = max(contours, key=cv2.contourArea)

    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    if angle < -45:
        angle += 90
    else:
        angle -= 90

    rotation_matrix = cv2.getRotationMatrix2D((x, y), angle, 1.0)
    height, width = image.shape[:2]
    cos_angle = np.abs(rotation_matrix[0, 0])
    sin_angle = np.abs(rotation_matrix[0, 1])
    new_width = int(height * sin_angle + width * cos_angle)
    new_height = int(height * cos_angle + width * sin_angle)
    rotation_matrix[0, 2] += (new_width / 2) - x
    rotation_matrix[1, 2] += (new_height / 2) - y
    image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

    x1 = int(x + w/2)
    y1 = int(y - h/2)
    x2 = int(x + w/2)
    y2 = int(y + h/2)

    #print(f'y = {k}x + {b}')

    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)



