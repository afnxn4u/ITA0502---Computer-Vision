import cv2
import numpy as np

def detect_vehicles():
    # Load the pre-trained car cascade classifier
    car_cascade = cv2.CascadeClassifier('28-cars.xml')
    
    cap = cv2.VideoCapture('28-vehicles.mp4')
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)
        
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Vehicle', (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        cv2.imshow('Vehicle Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_vehicles()