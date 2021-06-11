import cv2 as cv

cap = cv.VideoCapture(0)

def changeRes(width, height):
    cap.set(3, width)
    cap.set(4, height)

changeRes(1000, 600)

haar_casc = cv.CascadeClassifier('haar_fullbody.xml')

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = haar_casc.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=1)
    
    cv.imshow('Cam 0', frame)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()