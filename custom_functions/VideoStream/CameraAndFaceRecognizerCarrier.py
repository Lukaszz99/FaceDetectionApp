from custom_functions.VideoStream import WebCamStream
from custom_functions.FaceRecognizer import FaceRecognizer


class CameraAndFaceRecognizerCarrier:
    def __init__(self, camName, location, encodings, src=0):
        self.camName = camName
        self.location = location
        self.encodings = encodings
        self.src = src

    def start_carrier(self):
        self._init_camera()
        self._init_FaceRecognizer()

    def _init_camera(self):
        self.cam = WebCamStream.WebCamStream(src=self.src, name=self.camName,
                                             location=self.location).start()
        print('{} in {} started'.format(self.cam.name, self.cam.location))

    def _init_FaceRecognizer(self):
        FR_name = "{}_recognizer".format(self.camName)
        self.recognizer = FaceRecognizer.FaceRecognizer(name=FR_name,
                                                        encodings=self.encodings, related_video_stream=self.cam)
        self.recognizer.start()
