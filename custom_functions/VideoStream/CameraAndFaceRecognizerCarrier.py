from custom_functions.VideoStream import WebCamStream
from custom_functions.FaceRecognizer import FaceRecognizer


class CameraAndFaceRecognizerCarrier:
    """This class is carrier for both WebCamStream and FaceRecognizer

    Args:
        camName (str): camera name.
        location (str): location of camera, use one Locations from Locations.py.
        encodings (dict): .pickle file with encoded faces.
        min_time (float): minimum amount of time a person must be recognized to gain access.
        src (int or str): camera stream source. 0 - hardware camera or URL of video stream. Default 0.
        detect_method (str): method for face encoding 'hog' or 'cnn'. Default 'cnn'.
        scale (float): frame scaling for face recognition, use 1.0 if you have powerful CPU or 0.5 for more FPS. Lower scale lowers recognition accuracy. Default 0.5.
    """
    def __init__(self, camName, location, encodings, min_time, src=0, detect_method='cnn', scale=0.5):
        self.camName = camName
        self.location = location
        self.encodings = encodings
        self.min_time = min_time
        self.src = src
        self.detect_method = detect_method
        self.scale = scale

    def is_access_granted(self):
        """
        Return:
             True if access in camera's location is granted
        """
        return self.recognizer.is_access_granted()

    def start_carrier(self):
        """Initialize WebCameraStream and FaceRecognizer classes"""
        self._init_camera()
        self._init_FaceRecognizer()

    def _init_camera(self):
        self.cam = WebCamStream.WebCamStream(name=self.camName, location=self.location,
                                             src=self.src).start()

        # info when camera started
        print('{} in {} started'.format(self.cam.name, self.cam.location))

    def _init_FaceRecognizer(self):
        FR_name = "{}_recognizer".format(self.camName)
        self.recognizer = FaceRecognizer.FaceRecognizer(
            name=FR_name, encodings=self.encodings, min_time=self.min_time, related_video_stream=self.cam,
            detect_method=self.detect_method, scale=self.scale)
        self.recognizer.start()
