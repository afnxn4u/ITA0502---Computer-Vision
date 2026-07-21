import cv2
import numpy as np

img = cv2.imread("Input/Image 4.png")

if img is not None:
    kernel = np.ones((5, 5), np.uint8)
    dilated_img = cv2.dilate(img, kernel, iterations=1)
    cv2.imwrite("dilated_output.jpg", dilated_img)
    cv2.imshow("Original", img)
    cv2.imshow("Dilated", dilated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")