"""
| The core module of Face Recognition App
| You can run app from command line by typing
| python main.py -e path_to_encoded_faces.pickle -d detect_method
| detect_method is one of 'hog' or 'cnn'
"""

import argparse
import pickle
from threading import Thread
import time
from custom_functions.VideoStream import CameraAndFaceRecognizerCarrier


def main():
    """| Inside main function CameraAndFaceRecognizerCarrier is started to maintain camera and face recognizer module"""
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--encodings", required=True,
                    help="path to serialized db of facial encodings")
    ap.add_argument("-d", "--detect_method", type=str, default="cnn",
                    help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())

    data = pickle.loads(open(args["encodings"], "rb").read())
    print('Encodings loaded.')

    WebCam1_Lab1 = CameraAndFaceRecognizerCarrier.CameraAndFaceRecognizerCarrier(
        camName='WebCam1', location='Lab1', encodings=data, min_time=2.5,
        src=0, detect_method=args['detect_method'], scale=0.5)
    WebCam1_Lab1.start_carrier()

    # example how to checking access on camera's location

#    def check_access():
#       while not WebCam1_Lab1.recognizer.stopped:
#            # check access every 1 sec
#        time.sleep(1.0)
#        if WebCam1_Lab1.is_access_granted():
#            print("{} in {}: Access granted!".format(WebCam1_Lab1.camName, WebCam1_Lab1.location))

#    access_check_thread = Thread(target=check_access)
#    access_check_thread.start()


if __name__ == '__main__':
    main()
