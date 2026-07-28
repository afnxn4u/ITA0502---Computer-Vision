import cv2
import numpy as np

# Open input video
cap = cv2.VideoCapture("Input/vid 6.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("Output/Perspective_Video.mp4", fourcc, fps, (width, height))

# Source points
pts1 = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
])

# Destination points
pts2 = np.float32([
    [0, 0],
    [width, 50],
    [100, height],
    [width - 100, height]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    transformed = cv2.warpPerspective(frame, matrix, (width, height))

    out.write(transformed)

    cv2.imshow("Perspective Video", transformed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()