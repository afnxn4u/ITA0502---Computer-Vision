import cv2
import numpy as np

# Read image
image = cv2.imread("Input/Image 14.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

rows, cols = image.shape[:2]

# Source points
src_pts = np.float32([
    [50,50],
    [300,50],
    [50,300],
    [300,300]
])

# Destination points
dst_pts = np.float32([
    [10,100],
    [280,20],
    [80,300],
    [320,280]
])

# Homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply Homography
result = cv2.warpPerspective(image, H, (cols, rows))

# Save output
cv2.imwrite("Output/Homography_Output.png", result)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()