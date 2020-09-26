"""
Author: Łukasz Sawicki
Mail: l.saw99@outlook.com
"""
# HOW TO RUN python main.py -e your_encodings.pickle -d detect_method

import argparse
import pickle
from threading import Thread
import time
from custom_functions.VideoStream import CameraAndFaceRecognizerCarrier


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--encodings", required=True,
                    help="path to serialized db of facial encodings")
    ap.add_argument("-d", "--detect_method", type=str, default="cnn",
                    help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())

    data = pickle.loads(open(args["encodings"], "rb").read())
    print('Encodings loaded.')

    # this carrier is for one camera
    # each camera has related FaceRecognizer object
    # camName should be unique
    # you should choose one of existing location (in custom_functions/Access/Locations.py)

    # variables description
    # camName - name of camera, please keep it unique
    # location - location of camera, should be on of locations from custom_functions/Access/Locations.py
    # locations given in this folder are only for app testing.
    # encodings = .pickle file with known coded faces for recognition, you can make your own .pickle file
    # min_time - minimum amount of time a person must be recognized to gain access
    # src - camera video source, 0 is for hardware build-in camera.
    # You can pass IP address, checkOpenCV VideoCapture manual for more
    # detect_method - given in arguments, hog or cnn
    # scale - frame scaling for face recognition, use 1.0 if you have powerful CPU
    # or 0.5 for more FPS. Lower scale lowers recognition accuracy
    WebCam1_Lab1 = CameraAndFaceRecognizerCarrier.CameraAndFaceRecognizerCarrier(
        camName='WebCam1', location='Lab1', encodings=data, min_time=2.5,
        src=0, detect_method=args['detect_method'], scale=0.5)
    WebCam1_Lab1.start_carrier()

    # example how to checking access on camera's location

    def check_access():
        while not WebCam1_Lab1.recognizer.stopped:
            # check access every 1 sec
            time.sleep(1.0)
            if WebCam1_Lab1.is_access_granted():
                print("{} in {}: Access granted!".format(WebCam1_Lab1.camName, WebCam1_Lab1.location))

    access_check_thread = Thread(target=check_access)
    access_check_thread.start()


if __name__ == '__main__':
    main()
