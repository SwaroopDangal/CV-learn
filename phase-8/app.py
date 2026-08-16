import cv2

face_cascade = cv2.CascadeClassifier("phase-8\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,5)
    #1.1-> scale factor,5->min neighbors

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Webcam face detection",frame)

    if cv2.waitKey(1):
        break


cap.release()
cv2.destroyAllWindows()
