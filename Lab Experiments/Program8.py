import cv2

# Read image from Input folder
image = cv2.imread("Input/Image 8.png")

if image is None:
    print("Error: Could not read the image.")
    exit()

# Get original dimensions
height, width = image.shape[:2]

# Scale to bigger size (2x)
bigger = cv2.resize(image, (width * 2, height * 2))

# Scale to smaller size (0.5x)
smaller = cv2.resize(image, (width // 2, height // 2))

# Save output images
cv2.imwrite("Output/Bigger_Image.png", bigger)
cv2.imwrite("Output/Smaller_Image.png", smaller)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()