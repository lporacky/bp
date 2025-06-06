import ximea.xiapi as xiapi
import cv2
from functions import *
import os
from datetime import datetime
from data.rois import *
from data.color_data import *
GRID_SIZE = (3, 3)


def count_cells(hsv_matrix, lower, upper):
    return sum(lower[0] <= h <= upper[0] and lower[1] <= s <= upper[1] and lower[2] <= v <= upper[2]
               for h, s, v in hsv_matrix)

# Inicializácia kamery
cam = xiapi.Camera()
cam.open_device()
# max_width = cam.get_param("width")
# max_height = cam.get_param("height")
# print(f"Max: {max_width}x{max_height}")

# cam.set_param('width', 2464)
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

cv2.namedWindow("Live Detection", cv2.WINDOW_NORMAL)

try:
    while True:
        cam.get_image(img)
        frame = img.get_image_data_numpy()
        output = frame.copy()
        h, w = output.shape[:2]
        box_count = 0

        for idx, box in enumerate(boxes_def):
            empty_squares = 0
            for (xr, yr, wr, hr) in box:
                x = int(xr * w)
                y = int(yr * h)
                ww = int(wr * w)
                hh = int(hr * h)

                roi = output[y:y + hh, x:x + ww]
                hsv_matrix = extract_color_matrix(roi)
                brown = count_cells(hsv_matrix, lower_box, upper_box)

                roi_color = (0, 0, 255) if brown >= 5 else (0, 255, 0)
                if brown >= 5:
                    empty_squares += 1
                cv2.rectangle(output, (x, y), (x + ww, y + hh), roi_color, 2)

            (x0r, y0r, _, _) = box[0]
            (x1r, y1r, w1r, h1r) = box[3]
            x0 = int(x0r * w)
            y0 = int(y0r * h)
            x1 = int(x1r * w + w1r * w)
            y1 = int(y1r * h + h1r * h)

            large_roi = frame[y0:y1, x0:x1]
            dominant_color = get_dominant_color(large_roi)
            dominant_color_name = dominant_color[0]

            box_color = (0, 0, 255) if empty_squares == 4 else (0, 255, 0)
            if empty_squares < 4:
                box_count += 1
            cv2.rectangle(output, (x0, y0), (x1, y1), box_color, 3)

            cv2.putText(output, dominant_color_name, (x0, y0 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.putText(output, f'Detekovane boxy: {box_count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Live Detection", output)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC
            break
        elif key == ord('s'):  # 's' na uloženie snímky
            save_dir = r"C:\Users\plibo\Desktop\BP\vzorky\kamera\nove"
            os.makedirs(save_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"snimok_{timestamp}.jpg"
            filepath = os.path.join(save_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"Obraz uložený: {filepath}")

finally:
    cam.stop_acquisition()
    cam.close_device()
    cv2.destroyAllWindows()
