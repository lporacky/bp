import ximea.xiapi as xiapi
import cv2 as cv
import numpy as np
import time
from collections import Counter
from data.color_data import *
from data.rois import *
from functions import get_dominant_color, get_rectangle_roi

# Inicializácia kamery
cam = xiapi.Camera()
cam.open_device()
cam.set_param('width', 2056)
cam.set_param('height', 2056)
cam.set_param('offsetX', 200)
cam.set_param('offsetY', 0)
cam.set_exposure(7000)
cam.set_gain(10)
cam.set_param("imgdataformat", "XI_RGB24")
cam.set_param("auto_wb", 1)
cam.start_acquisition()
img = xiapi.Image()

cv.namedWindow("Live", cv.WINDOW_NORMAL)
last_processed_time = time.time()

try:
    while True:
        cam.get_image(img)
        frame = img.get_image_data_numpy()

        current_time = time.time()
        if current_time - last_processed_time >= 2:
            print("[INFO] Spracúvam frame")

            box_count = 0
            real_comb = []

            image_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            white_mask = cv.inRange(image_hsv, lower_white, upper_white)
            morph = cv.GaussianBlur(white_mask, (5, 5), 0)
            contours, _ = cv.findContours(morph, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            cv.imshow("Live", white_mask)
            for contour in contours:
                area = cv.contourArea(contour)
                if min_area < area:
                    box_count += 1

            if box_count == 6:
                for i, (xr, yr, wr, hr) in enumerate(giant_boxes):
                    hsv_roi = get_rectangle_roi(frame, image_hsv, i + 1, xr, yr, wr, hr)
                    dominant_color = get_dominant_color(hsv_roi)
                    print(dominant_color)
                    real_comb.append(dominant_color[0])

                if Counter(comb1) == Counter(real_comb) or Counter(comb2) == Counter(real_comb):
                    print("OK")
                else:
                    print("NOK")
            else:
                print("NOK")

            last_processed_time = current_time

        # cv.imshow("Live", frame)

        key = cv.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break

finally:
    cam.stop_acquisition()
    cam.close_device()
    cv.destroyAllWindows()
