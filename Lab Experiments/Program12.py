import cv2
import numpy as np

# Read image
image = cv2.imread("Input/Image 12.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

rows, cols = image.shape[:2]

# Four corner points
pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])

# Destination points
pts2 = np.float32([[0,0],[300,0],[100,300],[250,300]])

# Perspective matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
perspective = cv2.warpPerspective(image, matrix, (cols, rows))

# Save output
cv2.imwrite("Output/Perspective_Image.png", perspective)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()