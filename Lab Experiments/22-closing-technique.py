import cv2
import numpy as np

def apply_closing(image_path, kernel_size=(5,5)):
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones(kernel_size, np.uint8)
    
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('Original Image', gray)
    cv2.imshow('Closing Result', closing)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "sample.jpg"
    
    apply_closing(image_path)
    
    # apply_closing(image_path, kernel_size=(7,7))