import cv2 as cv
from threading import Thread


class WebCamStream:
    """
    Class to maintain video source

    Args:
        name (str): camera name.
        src (int or str): camera stream source. 0 - hardware camera or URL of video stream. Default 0. For more check OpenCV VideoCapture.
        location (str): location of camera, use one Locations from Locations.py.
    """
    def __init__(self, name,  location, src=0):
        self.stream = cv.VideoCapture(src, cv.CAP_DSHOW)
        self.status, self.frame = self.stream.read()
        self.location = location
        self.name = name
        self.stopped = False

    def start(self):
        """Starts WebCamStream thread"""
        thread = Thread(target=self._update, name=self.name, args=())
        thread.start()
        return self

    def _update(self):
        while True:
            if self.stopped:
                return
            # while not stopped, return next frame
            self.status, self.frame = self.stream.read()

    def read(self):
        """Read one frame from video source"""
        return self.frame

    def stop(self):
        """Stops WebCamStream thread"""
        self.stream.release()
        self.stopped = True
