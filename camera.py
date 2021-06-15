import cv2
import time

class VideoCamera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.object_classifier = cv2.CascadeClassifier("models/cars.xml")
        self.last_epoch = 0

    def frame_analys(self):
        _, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        objects = self.object_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)


        if len(objects) and (time.time() - self.last_epoch) > 10000:
            self.last_epoch = time.time()
            crop_img_list = []
            for (x, y, w, h) in objects:
                crop_img = frame[y:y+h, x:x+w]
                ret, jpeg = cv2.imencode('.jpg', crop_img)
                crop_img_list.append(jpeg.tobytes())

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

        return (frame, len(objects))

    def get_frame(self):
        nframe = self.frame_analys()
        text = cv2.putText(nframe[0], "Objects: {}".format(nframe[1]), (450,25), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0,0),2)
        ret, jpeg = cv2.imencode('.jpg', nframe[0])
        return jpeg.tobytes()


