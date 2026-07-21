import cv2
import numpy as np

# Read image from Input folder
image = cv2.imread("Input/Image 10.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Translation values
tx = 100   # Move right by 100 pixels
ty = 50    # Move down by 50 pixels

# Translation matrix
translation_matrix = np.float32([[1, 0, tx],
                                 [0, 1, ty]])

# Apply translation
translated = cv2.warpAffine(image, translation_matrix, (width, height))

# Save output
cv2.imwrite("Output/Translated_Image.png", translated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

cv2.waitKey(0)
cv2.destroyAllWindows()