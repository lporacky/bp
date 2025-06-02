import ximea.xiapi as xiapi
import cv2
import numpy as np

def nothing(x):
    pass

# Inicializácia kamery
cam = xiapi.Camera()
cam.open_device()

# Nastavenie parametrov kamery (prispôsob si podľa potreby)
cam.set_param('width', 2056)
cam.set_param('height', 2056)
cam.set_param("offsetX", 200)
cam.set_param("offsetY", 0)
cam.set_exposure(7000)
cam.set_gain(10)
cam.set_param("imgdataformat", "XI_RGB24")
cam.set_param("auto_wb", 1)

# Začatie akvizície
cam.start_acquisition()
img = xiapi.Image()

# Trackbar okno
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

print("Stlač ESC na ukončenie, 's' na uloženie HSV hodnôt.")

while True:
    cam.get_image(img)
    frame = img.get_image_data_numpy()

    # Zmenši snímku pre rýchlejšie spracovanie a zobrazenie (voliteľné)
    frame_resized = cv2.resize(frame, (520, 360))

    hsv = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    lower_range = np.array([l_h, l_s, l_v])
    upper_range = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(frame_resized, frame_resized, mask=mask)
    mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stacked = np.hstack((mask_3, frame_resized, res))

    cv2.imshow('Trackbars', stacked)

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break
    elif key == ord('s'):
        hsv_values = [[l_h, l_s, l_v], [u_h, u_s, u_v]]
        np.save('hsv_value', hsv_values)
        print("HSV hodnoty uložené:", hsv_values)

cam.stop_acquisition()
cam.close_device()
cv2.destroyAllWindows()
