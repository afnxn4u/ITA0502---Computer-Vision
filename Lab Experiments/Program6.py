import cv2
import time

# Load video from Input folder
video = cv2.VideoCapture("Input/vid 6.mp4")

if not video.isOpened():
    print("Error: Could not open video.")
    exit()

print("Press:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

delay = 30  # Normal speed

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video Player", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        delay = 100      # Slow motion
        print("Slow Motion")
    elif key == ord('f'):
        delay = 10       # Fast motion
        print("Fast Motion")
    elif key == ord('n'):
        delay = 30       # Normal speed
        print("Normal Speed")

video.release()
cv2.destroyAllWindows()