import cv2

# Open the default webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

delay = 30  # Normal speed

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('s'):
        delay = 100   # Slow motion
        print("Slow Motion")
    elif key == ord('f'):
        delay = 10    # Fast motion
        print("Fast Motion")
    elif key == ord('n'):
        delay = 30    # Normal speed
        print("Normal Speed")

camera.release()
cv2.destroyAllWindows()