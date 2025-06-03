# finding hsv range of target object(pen)
import cv2
import numpy as np

# A required callback method that goes into the trackbar function.
def find_hsv_range(image):
    def nothing(x):
        pass

    frame = cv2.resize(image, (1250, 1250))

    if frame is None:
        print("Error: Image not found.")
        exit()

    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    while True:
        # Convert the BGR image to HSV image.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get the new values of the trackbar in real time as the user changes
        # them
        l_h = cv2.getTrackbarPos("L - H", "Trackbars")
        l_s = cv2.getTrackbarPos("L - S", "Trackbars")
        l_v = cv2.getTrackbarPos("L - V", "Trackbars")
        u_h = cv2.getTrackbarPos("U - H", "Trackbars")
        u_s = cv2.getTrackbarPos("U - S", "Trackbars")
        u_v = cv2.getTrackbarPos("U - V", "Trackbars")

        # Set the lower and upper HSV range according to the value selected
        # by the trackbar
        lower_range = np.array([l_h, l_s, l_v])
        upper_range = np.array([u_h, u_s, u_v])

        # Filter the image and get the binary mask, where white represents
        # your target color
        mask = cv2.inRange(hsv, lower_range, upper_range)

        # You can also visualize the real part of the target color (Optional)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        # Converting the binary mask to a 3-channel image, this is just so
        # we can stack it with the others
        mask_3 = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Stack the mask, original frame, and the filtered result
        stacked = np.hstack((mask_3, frame, res))
        # stacked = np.hstack((mask_3, res))

        # Show this stacked frame at 40% of the size.
        cv2.imshow('Trackbars', cv2.resize(stacked, None, fx=0.4, fy=0.4))

        # If the user presses ESC then exit the program
        key = cv2.waitKey(1)
        if key == 27:
            break

        # If the user presses `s` then print this array.
        if key == ord('s'):
            thearray = [[l_h, l_s, l_v], [u_h, u_s, u_v]]
            print(thearray)

            # Also save this array as penval.npy
            # np.save('hsv_value', thearray)
            break

    # Destroy the windows.
    cv2.destroyAllWindows()


image1 = cv2.imread(r"C:\Users\plibo\Desktop\BP\just_try\6\snimok_20250529_085006.jpg")
image2 = cv2.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_6\snimok_20250529_084553.jpg")
image3 = cv2.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\6\snimok_20250507_135130.jpg")
image4 = cv2.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\light_6\snimok_20250529_084912.jpg")
image5 = cv2.imread(r"C:\Users\plibo\Desktop\BP\vzorky\kamera\6\snimok_20250529_084553.jpg")
find_hsv_range(image1)