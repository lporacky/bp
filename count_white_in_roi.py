import cv2 as cv
from data.color_data import *
from functions import *
from data.rois import *


def count_white_in_roi(image):
    box_count = 0
    image_hsv=cv.cvtColor(image, cv.COLOR_BGR2HSV)

    for i, (xr, yr, wr, hr) in enumerate(giant_boxes):
        hsv_roi = get_rectangle_roi(image, image_hsv, i + 1, xr, yr, wr, hr)
        white_count = count_pixels(lower_white, upper_white, hsv_roi)
        if white_count > min_area/2:
            # draw_rectangle_roi(image, image_hsv, i + 1, xr, yr, wr, hr)
            # print(white_count)
            box_count += 1

    # while True:
    #     if cv.waitKey(0) == ord('x'):
    #         break
    # cv.destroyAllWindows()

    # print(box_count)
    return box_count
