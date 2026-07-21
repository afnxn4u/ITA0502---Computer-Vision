import cv2

img = cv2.imread("Input/Image 2.png")

if img is not None:
    blurred_img = cv2.GaussianBlur(img, (15, 15), 0)
    cv2.imwrite("blurred_output.jpg", blurred_img)
    cv2.imshow("Original", img)
    cv2.imshow("Gaussian Blur", blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")