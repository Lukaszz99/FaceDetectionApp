import cv2 as cv
from threading import Thread


class WebCamStream:
    def __init__(self, src=0, name="WebCamStream", location=None):
        # 0 is for default hardware cam
        # src could be also a IP of camera
        # for more check OpenCV VideoCapture manual
        self.stream = cv.VideoCapture(src, cv.CAP_DSHOW)
        self.status, self.frame = self.stream.read()
        self.location = location
        self.name = name
        self.stopped = False

    def start(self):
        thread = Thread(target=self.update, name=self.name, args=())
        thread.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return
            # while not stopped, return next frame
            self.status, self.frame = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stream.release()
        self.stopped = True
