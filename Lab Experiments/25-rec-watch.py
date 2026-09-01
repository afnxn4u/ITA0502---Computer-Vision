import cv2
import numpy as np

def detect_watch(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image")
        return

    net = cv2.dnn.readNetFromCaffe(
        'models/MobileNetSSD_deploy.prototxt',
        'models/MobileNetSSD_deploy.caffemodel'
    )

    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor", "watch"]

    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    (h, w) = image.shape[:2]

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.2:
            class_id = int(detections[0, 0, i, 1])
            
            if CLASSES[class_id] == "watch":
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                label = f"Watch: {confidence * 100:.2f}%"
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(image, label, (startX, y), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Watch Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "sample.jpg"
    detect_watch(image_path)