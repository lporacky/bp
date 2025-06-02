import os
from otsu_method import *
from threshold_white import *
folder_path = 'C:/Users/plibo/Desktop/BP/vzorky/kamera/6/'

def try_directory(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp", ".tif")):
            file_path = os.path.join(folder_path, filename)
            image = cv.imread(file_path)
            result = threshold_white(image)

            if result == 6:
                print("OK")
            else:
                print("NOK")
            # otsu(image)

try_directory(folder_path)