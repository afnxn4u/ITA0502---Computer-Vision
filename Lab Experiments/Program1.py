import cv2
image = cv2.imread("Input/Image 1.png")
if image is not None:
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale_output.jpg", gray_img)
    cv2.imshow("Original", image)
    cv2.imshow("Grayscale", gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")