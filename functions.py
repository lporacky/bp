import cv2 as cv
import numpy as np
from data import color_data


def count_pixels(lower, upper, image):
    mask = cv.inRange(image, lower, upper)
    pixel_count = cv.countNonZero(mask)
    return pixel_count

def do_morph(after_mask, kernel_size=(3,3)):
    kernel = np.ones(kernel_size, np.uint8)
    opened = cv.morphologyEx(after_mask, cv.MORPH_OPEN, kernel)
    closed = cv.morphologyEx(opened, cv.MORPH_CLOSE, kernel)
    return closed


def extract_color_matrix(roi_img):
    grid_size = (3, 3)
    hsv_img = cv.cvtColor(roi_img, cv.COLOR_BGR2HSV)
    h, w = hsv_img.shape[:2]
    gh, gw = h // grid_size[0], w // grid_size[1]
    matrix = []
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            cell = hsv_img[i*gh:(i+1)*gh, j*gw:(j+1)*gw]
            mean = cell.mean(axis=(0, 1)).astype(int)
            matrix.append(mean.tolist())
    return matrix


def get_input():
    comb = []
    print("Farebne kombinacie:")
    print("[ Hedge Green,")
    print("  Cork,")
    print("  Raw Umber,")
    print("  Whitecap Gray,")
    print("  Gray Clouds  ]")

    for i in range(6):
        x = str(input("Vloz farbu cumlika:"))
        comb.append(x)

    return comb


def get_dominant_color(image):
    dominant_color = color_data.hsv_limits_doma[0]
    dom_pixels = 0
    for color in color_data.hsv_limits_doma:
        pixel_count = count_pixels(color[1], color[2], image)
        if dom_pixels < pixel_count:
            dom_pixels = pixel_count
            dominant_color = color
    return dominant_color

def count_brown(hsv_matrix, lower, upper):
    count = 0
    for row in hsv_matrix:
        for h, s, v in row:
            if lower[0] <= h <= upper[0] and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]:
                count += 1
    return count

def roi_box_count(image_path):
    image = cv.cvtColor(cv.imread(image_path), cv.COLOR_BGR2RGB)
    img_h, img_w = image.shape[:2]

    GRID_SIZE = (3, 3)
    lower_brown = (10, 50, 20)
    upper_brown = (20, 230, 255)

    # Definícia boxov: každý obsahuje 4 ROI oblasti
    boxes_def = [
        [
            (0.1, 0.1, 0.05, 0.05), (0.25, 0.1, 0.05, 0.05),
            (0.1, 0.35, 0.05, 0.05), (0.25, 0.35, 0.05, 0.05)
        ],
        [
            (0.4, 0.1, 0.05, 0.05), (0.55, 0.1, 0.05, 0.05),
            (0.4, 0.35, 0.05, 0.05), (0.55, 0.35, 0.05, 0.05)
        ],
        [
            (0.7, 0.1, 0.05, 0.05), (0.85, 0.1, 0.05, 0.05),
            (0.7, 0.35, 0.05, 0.05), (0.85, 0.35, 0.05, 0.05)
        ],
        [
            (0.1, 0.6, 0.05, 0.05), (0.25, 0.6, 0.05, 0.05),
            (0.1, 0.85, 0.05, 0.05), (0.25, 0.85, 0.05, 0.05)
        ],
        [
            (0.4, 0.6, 0.05, 0.05), (0.55, 0.6, 0.05, 0.05),
            (0.4, 0.85, 0.05, 0.05), (0.55, 0.85, 0.05, 0.05)
        ],
        [
            (0.7, 0.6, 0.05, 0.05), (0.85, 0.6, 0.05, 0.05),
            (0.7, 0.85, 0.05, 0.05), (0.85, 0.85, 0.05, 0.05)
        ]
    ]


    box_count = 0

    for box_index, box in enumerate(boxes_def):
        empty_squares = 0
        for roi_index, (xr, yr, wr, hr) in enumerate(box):
            x = int(xr * img_w)
            y = int(yr * img_h)
            w = int(wr * img_w)
            h = int(hr * img_h)

            roi_img = image[y:y + h, x:x + w]
            color_matrix = extract_color_matrix(roi_img, grid_size=GRID_SIZE)

            brown_pixels = count_brown(color_matrix, lower_brown, upper_brown)


            if brown_pixels >= 6:
                empty_squares += 1


        # Vyhodnotenie celej krabice
        if empty_squares < 4:
            box_count += 1

    print(f"Detected boxes: {box_count} name: {image_path[-10:-1]}")
    return box_count

def draw_countour(image, hsv_image, contour, box_index):
    # Nakresli kontúru do HSV obrazu (len na vizualizáciu)
    cv.drawContours(hsv_image, [contour], -1, (0, 255, 0), 2)

    # Vytvor masku a extrahuj časť obrazu vo vnútri kontúry
    mask = cv.drawContours(np.zeros(image.shape[:2], np.uint8), [contour], -1, 255, -1)
    roi = cv.bitwise_and(image, image, mask=mask)
    hsv_roi=cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    dominant = get_dominant_color(hsv_roi)
    print(dominant)
    # Preveď na zobraziteľný formát a zobraz v okne
    roi = cv.resize(roi, (700, 700))
    cv.imshow(f"box{box_index}", roi)

def draw_rectangle_roi(image, hsv_image, box_index, xr, yr, wr, hr):
    img_h, img_w = image.shape[:2]
    x = int(xr * img_w)
    y = int(yr * img_h)
    w = int(wr * img_w)
    h = int(hr * img_h)

    # Nakresli obdĺžnik do HSV obrazu (napr. na vizualizáciu)
    cv.rectangle(hsv_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Vyrež ROI (Region of Interest)
    roi = image[y:y + h, x:x + w]
    hsv_roi = hsv_image[y:y + h, x:x + w]
    dominant = get_dominant_color(hsv_roi)
    print(dominant)
    # Priprav na zobrazenie
    roi = cv.resize(roi, (700, 700))
    cv.imshow(f"box{box_index}", roi)

def dominant_color_of_roi(hsv_roi):
    dominant = get_dominant_color(hsv_roi)
    print(dominant)
    return dominant


def get_rectangle_roi(image, hsv_image, box_index, xr, yr, wr, hr):
    img_h, img_w = image.shape[:2]
    x = int(xr * img_w)
    y = int(yr * img_h)
    w = int(wr * img_w)
    h = int(hr * img_h)

    # Vyrež ROI (Region of Interest)
    roi = image[y:y + h, x:x + w]
    hsv_roi = hsv_image[y:y + h, x:x + w]
    return hsv_roi