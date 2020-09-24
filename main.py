"""
Author: Łukasz Sawicki
Mail: l.saw99@outlook.com
"""
# HOW TO RUN python main.py -e your_encodings.pickle -d detect_method

import argparse
import pickle
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
    WebCam1_Lab1 = CameraAndFaceRecognizerCarrier.CameraAndFaceRecognizerCarrier(
        camName='WebCam1', location='Lab1', encodings=data, src=0, detect_method=args['detect_method']).start_carrier()


if __name__ == '__main__':
    main()
