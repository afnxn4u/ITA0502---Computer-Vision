import cv2
import numpy as np

def apply_black_hat(image_path, kernel_size=(7,7)):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

    black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('Original Image', gray)
    cv2.imshow('Black Hat', black_hat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "sample.jpg"
    
    try:
        apply_black_hat(image_path)
    except Exception as e:
        print(f"Error: {e}")