import os
from count_white_in_roi import count_white_in_roi
from otsu_method import *
from threshold_white import *
folder_path = 'C:/Users/plibo/Desktop/BP/just_try/6/'

def try_directory(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp", ".tif")):
            file_path = os.path.join(folder_path, filename)
            image = cv.imread(file_path)
            result = threshold_white(image)
            # result = otsu(image)
            # result = count_white_in_roi(image)

try_directory(folder_path)