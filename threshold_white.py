import cv2 as cv
from data.color_data import *
from functions import *
from data.rois import *
from collections import Counter





def threshold_white(image):
    box_count = 0
    real_comb = []
    image_hsv=cv.cvtColor(image, cv.COLOR_BGR2HSV)
    white_mask=cv.inRange(image_hsv, lower_white, upper_white)

    morph = cv.GaussianBlur(white_mask, (5, 5), 0)


    contours, _ = cv.findContours(morph, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # SPOCITANIE KRABIC
    for contour in contours:
        area = cv.contourArea(contour)
        if min_area < area:
            box_count += 1


    # VYKRESLENIE NAJDENYCH KONTUR
    # box_index = 0
    # for contour in contours:
    #     area = cv.contourArea(contour)
    #     if min_area < area:
    #         box_index += 1
    #         draw_countour(image, image_hsv, contour, box_index)
    # while True:
    #     if cv.waitKey(0) == ord('x'):
    #         break
    # cv.destroyAllWindows()

    print(box_count)
    if box_count == 6:
        for i, (xr, yr, wr, hr) in enumerate(giant_boxes):
            # ZISKANIE FARBY CUMLIKA
            hsv_roi = get_rectangle_roi(image, image_hsv, i + 1, xr, yr, wr, hr)
            dominant_color = get_dominant_color(hsv_roi)
            # print(dominant_color)
            real_comb.append(dominant_color[0])

        # VYKRESLENIE 6 ROI NA POZICIACH JEDNOTLIVYCH KRABIC
        #     draw_rectangle_roi(image, image_hsv, i + 1, xr, yr, wr, hr)
        # while True:
        #     if cv.waitKey(0) == ord('x'):
        #         break
        # cv.destroyAllWindows()

        if Counter(comb1) == Counter(real_comb) or Counter(comb2) == Counter(real_comb):
            print("OK")
        else:
            print("NOK")

    else:
        print("NOK")



    # print(box_count)
    return box_count
