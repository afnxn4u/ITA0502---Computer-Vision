import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sample.jpg")
if img is None:
    raise Exception("Image not found")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)  # X direction
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)  # Y direction
combined_sobel = cv.magnitude(sobelx, sobely)

plt.figure(figsize=(12, 4))

plt.subplot(141), plt.imshow(img[:,:,::-1])
plt.title('Original'), plt.axis('off')

plt.subplot(142), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.axis('off')

plt.subplot(143), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.axis('off')

plt.subplot(144), plt.imshow(combined_sobel, cmap='gray')
plt.title('Combined Sobel'), plt.axis('off')

plt.show()
