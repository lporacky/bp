import os
import sys
from threshold_white import *

def try_directory(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".jpg", ".png", ".jpeg", ".bmp", ".tif")):
            file_path = os.path.join(folder_path, filename)
            image = cv.imread(file_path)
            result = threshold_white(image)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použitie: test_file.exe <cesta_k_priecinku>")
    else:
        folder_path = sys.argv[1]
        try_directory(folder_path)

print(os.cpu_count())