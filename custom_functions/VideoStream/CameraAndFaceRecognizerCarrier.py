"""
Author: Łukasz Sawicki
Mail: l.saw99@outlook.com
"""
# this class is carrier for both CamStream class and FaceRecognizerClass

from custom_functions.VideoStream import WebCamStream
from custom_functions.FaceRecognizer import FaceRecognizer


class CameraAndFaceRecognizerCarrier:
    def __init__(self, camName, location, encodings, min_time, src=0, detect_method='cnn', scale=0.5):
        self.camName = camName
        self.location = location
        self.encodings = encodings
        self.min_time = min_time
        self.src = src
        self.detect_method = detect_method
        self.scale = scale

    def is_access_granted(self):
        return self.recognizer.is_access_granted()

    def start_carrier(self):
        self._init_camera()
        self._init_FaceRecognizer()

    def _init_camera(self):
        self.cam = WebCamStream.WebCamStream(src=self.src, name=self.camName,
                                             location=self.location).start()

        # info when camera started
        print('{} in {} started'.format(self.cam.name, self.cam.location))

    def _init_FaceRecognizer(self):
        FR_name = "{}_recognizer".format(self.camName)
        self.recognizer = FaceRecognizer.FaceRecognizer(
            name=FR_name, encodings=self.encodings, min_time=self.min_time, related_video_stream=self.cam,
            detect_method=self.detect_method, scale=self.scale)
        self.recognizer.start()
