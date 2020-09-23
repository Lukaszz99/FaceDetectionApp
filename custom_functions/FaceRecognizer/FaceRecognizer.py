import cv2 as cv
import time
from threading import Thread
import face_recognition
from custom_functions.Drawing import drawing
from custom_functions.Access import AccessLevel


class FaceRecognizer:
    def __init__(self,name, encodings=None, related_video_stream=None, detect_method='cnn'):
        self.name = name
        self.encodings = encodings
        self.related_video_stream = related_video_stream
        self.detect_method = detect_method
        self.access_level = AccessLevel.AccessLevel()
        self.access_level.set_custom_accesses()
        self.stopped = False

    def start(self):
        # 2 sec for hardware to prepare cameras
        time.sleep(2.0)
        thread = Thread(target=self.recognize, name=self.name, args=())
        thread.start()
        return self

    def recognize(self):
        try:
            while True:
                if self.stopped:
                    return
                frame = self.related_video_stream.read()

                # BGR to RGB, because of face_recognition library
                rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

                # detect faceROI
                ROI = face_recognition.face_locations(rgb_frame,
                                                      model=self.detect_method)
                encodings = face_recognition.face_encodings(rgb_frame, ROI)
                names = []

                for encoding in encodings:
                    matches = face_recognition.compare_faces(self.encodings['encodings'], encoding)

                    # deafault if no face is recognize
                    name = 'Unknown'

                    if True in matches:
                        matchesIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}

                        for i in matchesIdxs:
                            name = self.encodings['names'][i]
                            counts[name] = counts.get(name, 0) + 1

                        name = max(counts, key=counts.get)

                    names.append(name)

                # check access of person in given location
                access = self.access_level.get_access(
                    names=names, location=self.related_video_stream.location)
                print(self.access_level.who_on_video(self.related_video_stream))

                # draw rectangle depends on access
                self._draw_rectangles(frame, ROI, names, access)

                # show frame on screen
                cv.imshow(self.related_video_stream.name, frame)

                # press 'q' to close program
                self._check_for_program_close()

        except NameError:
            print('Error in FaceRecognizer start method')

    def _draw_rectangles(self, frame, ROI, names, access):
        try:
            for ((top, right, bottom, left), name) in zip(ROI, names):

                if name == 'Unknown':
                    drawing.rectagne_unknow(frame, top, right, bottom, left)

                else:
                    for i in range(len(access)):
                        # [0] is to get first element from one-element list
                        name_idx = [x for x, y in enumerate(access) if y[0] == name][0]

                        if access[name_idx][1]:
                            drawing.rectangle_with_access(frame, name, top, right, bottom, left)
                        else:
                            drawing.rectangle_withOUT_access(frame, name, top, right, bottom, left)

        except NameError:
            print('Error in _draw_rectangles')

    def _check_for_program_close(self):
        key = cv.waitKey(1)
        if key == ord('q'):
            print('Closing program')
            cv.destroyAllWindows()
            self.stopped = True
            self.related_video_stream.stop()
            exit(0)
