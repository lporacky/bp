from data.color_data import *
import cv2 as cv

file_path = r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_6\snimok_20250529_084603.jpg"
image = cv.imread(file_path)

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

    thresh_otsu = cv.resize(thresh_otsu, (700, 700))
    cv.imshow("Otsu Threshold", thresh_otsu)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return box_count

otsu(image)
