import cv2



cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (25, 25), 0)
    
    cv2.imshow("original", frame)
    cv2.imshow("gray", gray)
    cv2.imshow("blur", blur)
    
    edges = cv2.Canny(gray, 100, 200)

    cv2.imshow("edges", edges)
    
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cap.release()
cv2.destoryAllWindows()