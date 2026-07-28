import cv2
import numpy as np

# Read image
image = cv2.imread("Input/Image 15.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

rows, cols = image.shape[:2]

# Source points
src = np.float32([
    [50,50],
    [300,50],
    [50,300],
    [300,300]
])

# Destination points
dst = np.float32([
    [20,80],
    [280,40],
    [80,300],
    [320,280]
])

# DLT using Perspective Transform
matrix = cv2.getPerspectiveTransform(src, dst)

result = cv2.warpPerspective(image, matrix, (cols, rows))

# Save output
cv2.imwrite("Output/DLT_Output.png", result)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Direct Linear Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()