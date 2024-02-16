import cv2
import numpy as np
import math

def detector(data: list, color_to_detect_low: list, color_to_detect_up: list, flag_fill: bool,  color_to_fill=[255, 255, 255], flag_dark=False):
    ''' 
    Signature:
    data: list - исходная картинка
    color_to_detect_low: list - нижняя граница цвета  
    color_to_detect_up: list - верхняя граница цвета
    flag_fill: bool - флаг, ставящийся, если нужно залить найденную область
    color_to_fill: list - цвет заливки
    flag_dark: bool - флаг, который ставится, если нужно залить черным все, кроме линий

    EX: detector(im, [20, 100, 100], [30, 255, 255], False)
    '''
    result = None

    hsv = cv2.cvtColor(data, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(color_to_detect_low), np.array(color_to_detect_up))
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   
    if flag_fill:
        for cnt in contours:
            cv2.fillPoly(data, [cnt], color_to_fill)
        result = data.copy()
        
        if flag_dark:
            for cnt in contours:
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                right_side_point1 = (box[1][0], box[1][1])
                right_side_point2 = (box[2][0], box[2][1])
            mask_combined = np.zeros_like(mask)
            for cnt in contours:
                cv2.fillPoly(mask_combined, [cnt], 255)
            result = cv2.bitwise_and(data, data, mask=mask_combined)
    else:
        result = cv2.drawContours(data.copy(), contours, -1, (255, 255, 255), 2)  # тут можно самим решить, как заливать
    return result
   





