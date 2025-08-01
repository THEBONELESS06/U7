import cv2, dlib, random

detector = dlib.get_frontal_face_detector()
cap = cv2.VideoCapture(0)
faces_colors = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for i, f in enumerate(faces):
        x, y, w, h = f.left(), f.top(), f.width(), f.height()
        faces_colors.setdefault(i, tuple(random.randint(0, 255) for _ in range(3)))
        cv2.rectangle(frame, (x, y), (x + w, y + h), faces_colors[i], 3)
    
    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
