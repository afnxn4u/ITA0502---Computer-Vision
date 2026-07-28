import cv2
import numpy as np

# Read image
image = cv2.imread("Input/Image 11.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

rows, cols = image.shape[:2]

# Select three points from the original image
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

# New positions of the selected points
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Affine Transformation Matrix
matrix = cv2.getAffineTransform(pts1, pts2)

# Apply transformation
affine = cv2.warpAffine(image, matrix, (cols, rows))

# Save output
cv2.imwrite("Output/Affine_Transformation.png", affine)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()