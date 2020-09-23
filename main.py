import argparse
import pickle
from custom_functions.VideoStream import CameraAndFaceRecognizerCarrier


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-e", "--encodings", required=True,
                    help="path to serialized db of facial encodings")
    ap.add_argument("-d", "--detection-method", type=str, default="cnn",
                    help="face detection model to use: either `hog` or `cnn`")
    args = vars(ap.parse_args())

    data = pickle.loads(open(args["encodings"], "rb").read())
    print('Encodings loaded.')

    WebCam1_Lab1 = CameraAndFaceRecognizerCarrier.CameraAndFaceRecognizerCarrier(
        camName='WebCam1', location='Lab1', encodings=data, src=0).start_carrier()


if __name__ == '__main__':
    main()
