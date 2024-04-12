import cv2
import numpy as np

def detector_by_bgr(data, color_to_detect_low, color_to_detect_up, flag_fill, color_to_fill=[0, 255, 0], flag_dark=False):
    mask = cv2.inRange(data, np.array(color_to_detect_low), np.array(color_to_detect_up))
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if flag_fill:
        for cnt in contours:
            cv2.fillPoly(data, [cnt], color_to_fill)
        result = data.copy()

        if flag_dark:
            mask_combined = np.zeros_like(mask)
            for cnt in contours:
                cv2.fillPoly(mask_combined, [cnt], 255)
            result = cv2.bitwise_and(data, data, mask=mask_combined)
    else:
        result = cv2.drawContours(data.copy(), contours, -1, (255, 255, 255), 2)

    return result

if __name__ == '__main__':
    img = cv2.imread('ex.png')
    red_low =   [0,   0,     100]
    red_up  =   [100, 100,   255]

    out = detector_by_bgr(img, red_low, red_up, True)
    cv2.imwrite('out.png', out)
    cv2.imshow('out', out)
    cv2.waitKey(0)