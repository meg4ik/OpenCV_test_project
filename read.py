import cv2 as cv

cap = cv.VideoCapture(0)

def changeRes(width, height):
    cap.set(3, width)
    cap.set(4, height)

#changeRes(700, 400)

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #blur = cv.GaussianBlur(frame, (1,1), cv.BORDER_DEFAULT)
    canny = cv.Canny(gray, 100, 100)
    #text = cv.putText(canny, "Cam 0", (520,25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0,0),2)

    conturs, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    

    cv.imshow('Cam 0', canny)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()