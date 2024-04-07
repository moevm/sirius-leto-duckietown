import cv2
import numpy as np
def get_action(image):
    lower_bound = np.array([0,100,100])
    upper_bound = np.array([80,250,250])
    mask = cv2.inRange(image, lower_bound, upper_bound)
    #mask = cv2.bitwise_and(image, image, mask=mask)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 1)
    mask = cv2.dilate(mask, kernel, iterations = 1)
    

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print('Не видно контуров')
        return 0

    cnt = max(contours, key=cv2.contourArea)

    
    moments = cv2.moments(cnt)


    if moments['m00'] != 0:
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
    else:
        cx, cy = None, None
    print(f'cx = {cx} \t cy = {cy}')
    