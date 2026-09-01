import cv2
import numpy as np

def apply_tophat(image_path, kernel_size=(7,7)):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return None
    
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow('Original Image', gray)
    cv2.imshow('Top Hat Result', tophat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "sample.jpg"
    apply_tophat(image_path)