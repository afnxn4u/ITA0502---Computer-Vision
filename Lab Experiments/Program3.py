import cv2

img = cv2.imread("Input/Image 3.png")

if img is not None:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_img, 100, 200)
    cv2.imwrite("canny_output.jpg", edges)
    cv2.imshow("Original", img)
    cv2.imshow("Canny Outline", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read the image.")