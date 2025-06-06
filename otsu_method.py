from data.color_data import *
import cv2 as cv


def otsu(image):
    box_count = 0
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    morph = cv.GaussianBlur(image_gray, (5, 5), 0)
    _, thresh_otsu = cv.threshold(morph, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    contours, _ = cv.findContours(thresh_otsu, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv.contourArea(contour)
        if min_area < area:
            box_count += 1

    print(box_count)
    return box_count
