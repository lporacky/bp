import cv2 as cv
from data.color_data import *
from functions import *
from data.rois import *


def threshold_white(image):
    box_count = 0

    # image = image[100:-100, 100:-100]
    image_hsv=cv.cvtColor(image, cv.COLOR_BGR2HSV)
    white_mask=cv.inRange(image_hsv, lower_white, upper_white)

    morph = cv.GaussianBlur(white_mask, (5, 5), 0)


    contours, _ = cv.findContours(morph, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv.contourArea(contour)
        if min_area < area:
            box_count += 1



    # box_index = 0
    # for contour in contours:
    #     area = cv.contourArea(contour)
    #     if min_area < area:
    #         box_index += 1
    #         draw_countour(image, image_hsv, contour, box_index)
    if box_count == 6:
        for i, (xr, yr, wr, hr) in enumerate(giant_boxes):

            draw_rectangle_roi(image, image_hsv, i + 1, xr, yr, wr, hr)

        while True:
            if cv.waitKey(0) == ord('x'):
                break
        cv.destroyAllWindows()
        print("OK")
    else:
        print("NOK")



    # print(box_count)
    return box_count


image = cv.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_6\snimok_20250529_084749.jpg")
# image = cv.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_5\snimok_20250529_091627.jpg")
# image = cv.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_6\snimok_20250529_085220.jpg")
threshold_white(image)