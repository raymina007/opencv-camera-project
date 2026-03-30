import cv2

cap = cv2.VideoCapture(0)

mode = "original"

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    if mode == "original":
        display = frame
    elif mode == "gray":
        display = gray
    elif mode == "edge":
        display = edges

    cv2.imshow("camera", display)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('o'):
        mode = "original"
    elif key == ord('g'):
        mode = "gray"
    elif key == ord('e'):
        mode = "edge"
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()