import cv2
import numpy as np

def main():
    image = cv2.imread('sample.jpg', cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Error: Could not load image")
        return
    
    kernel = np.ones((5, 5), np.uint8)
    
    eroded_image = cv2.erode(image, kernel, iterations=1)
    
    cv2.imshow('Original Image', image)
    cv2.imshow('Eroded Image', eroded_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()