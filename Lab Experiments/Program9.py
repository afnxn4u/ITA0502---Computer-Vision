import cv2

# Read image from Input folder
image = cv2.imread("Input/Image 9.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Center of the image
center = (width // 2, height // 2)

# Rotate 90 degrees clockwise
clockwise_matrix = cv2.getRotationMatrix2D(center, -90, 1.0)
clockwise = cv2.warpAffine(image, clockwise_matrix, (width, height))

# Rotate 90 degrees counter-clockwise
counter_matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
counter = cv2.warpAffine(image, counter_matrix, (width, height))

# Save output images
cv2.imwrite("Output/Clockwise_Rotation.png", clockwise)
cv2.imwrite("Output/CounterClockwise_Rotation.png", counter)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter)

cv2.waitKey(0)
cv2.destroyAllWindows()