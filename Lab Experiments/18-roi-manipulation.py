import cv2

img = cv2.imread('sample.jpg')
if img is None:
    print("Error: Could not load image")
    exit()
img_copy = img.copy()

x, y = 100, 100
width, height = 200, 200
roi = img[y:y+height, x:x+width]

# Ensure destination coordinates don't exceed image boundaries
dest_x = min(300, img.shape[1] - width)
dest_y = min(300, img.shape[0] - height)

img_copy[dest_y:dest_y+height, dest_x:dest_x+width] = roi
cv2.imshow('Original Image', img)
cv2.imshow('Image with ROI copied', img_copy)

cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)
cv2.imshow('Original with ROI marked', img)

cv2.waitKey(0)
cv2.destroyAllWindows()