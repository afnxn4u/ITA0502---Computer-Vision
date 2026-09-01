import cv2
import numpy as np

image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Could not load image")
    exit()
    
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.uint8)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('After Opening', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('opening_result.jpg', opening)