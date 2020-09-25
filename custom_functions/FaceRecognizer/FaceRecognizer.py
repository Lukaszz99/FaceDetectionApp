"""
Author: Łukasz Sawicki
Mail: l.saw99@outlook.com
"""
import cv2 as cv
import time
from threading import Thread
import face_recognition
from custom_functions.Drawing import drawing
from custom_functions.Access import AccessLevel
from custom_functions.VideoStream import FrameCounter
from custom_functions.Access import AccesAfterTime


class FaceRecognizer:
    def __init__(self, name, encodings=None, related_video_stream=None, detect_method='cnn', scale=0.5):
        self.name = name
        self.encodings = encodings
        self.related_video_stream = related_video_stream
        self.detect_method = detect_method
        self.stopped = False

        # Smaller frame to recognize faces faster.
        # While working on GPU or on good performance CPU
        # don't need to make frame smaller (then set scale to 1.0)
        # smaller frame lower accuracy of recognition,
        # but increase FPS
        # SCALE MUST BE ONE OF: 0.5, 1.0
        # could be 0.25, but then you must have high resolution camera
        self.scale = scale

        # classes used inside recognize function
        self.access_level = AccessLevel.AccessLevel()
        self.access_level.set_custom_accesses()
        self.frame_counter = FrameCounter.FrameCounter()
        self.access_after_time = AccesAfterTime.AccessAfterTime()

    def start(self):
        # 2 sec for hardware to prepare cameras
        time.sleep(2.0)
        thread = Thread(target=self._display_result, name=self.name, args=())
        thread.start()
        return self

    def _display_result(self):
        while True:
            names, frame, ROI = self._recognize()

            # check access of person in given location
            # for drawing rectangles on faces
            access_for_person = self.access_level.get_access(
                names=names.copy(), location=self.related_video_stream.location)

            # draw rectangle over the face on frame depends on access
            self._draw_rectangles(frame, ROI, names.copy(), access_for_person)

            # put FPS on frame
            cv.putText(frame, 'FPS:' + str(self.frame_counter.get_FPS()),
                       (1, 18), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0))

            # show frame on screen
            cv.imshow(self.related_video_stream.name, frame)

            # here access is checking in proper way
            # every person seen on video is log with log system
            self.access_after_time.get_persons_from_frame(names.copy(), access_for_person, frame,
                                                          self.related_video_stream)
            self.access_after_time.log_access(self.related_video_stream)

            # check for access in location
            # of related camera
            access_in_location = self.access_after_time.access_in_location()
            print(access_in_location)

            # press 'q' to close program
            self._check_for_program_close()

    def _recognize(self):
        try:
            if self.stopped:
                return

            # read next frame from vide stream if program is not stopped
            frame = self.related_video_stream.read()

            # functions for calculating FPS in video stream
            self.frame_counter.frame_read()
            self.frame_counter.calculate_FPS()

            small_frame = cv.resize(frame, (0, 0), fx=self.scale, fy=self.scale)

            # BGR to RGB, because of face_recognition library
            rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)

            # detect face ROI on frame
            ROI = face_recognition.face_locations(rgb_small_frame,
                                                  model=self.detect_method)

            # make 128-dimensional vector from every face detected on frame
            # to compare with known faces
            encodings = face_recognition.face_encodings(rgb_small_frame, ROI)

            # list for keeping recognized names
            names = []

            # iterate over all encoded faces in frame and find persons's name of recognized faces
            for encoding in encodings:
                matches = face_recognition.compare_faces(self.encodings['encodings'], encoding)

                # deafault if no face is recognized
                name = 'Unknown'

                if True in matches:
                    matchesIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchesIdxs:
                        name = self.encodings['names'][i]
                        counts[name] = counts.get(name, 0) + 1

                    # name is choose by voting
                    name = max(counts, key=counts.get)

                names.append(name)

            # return recognized names, frame on which it was detected and face locations - ROI
            return names, frame, ROI

        except NameError:
            print('Error in FaceRecognizer start method')


    def _draw_rectangles(self, frame, ROI, names, access):
        try:
            for ((top, right, bottom, left), name) in zip(ROI, names):

                # resize frame to show normal size
                rescale = int(1 / self.scale)
                top *= rescale
                right *= rescale
                bottom *= rescale
                left *= rescale
                if name == "Unknown":
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

    # this function wait for 'q' pressed and closing program
    def _check_for_program_close(self):
        key = cv.waitKey(1)
        if key == ord('q'):
            print('Closing program')
            cv.destroyAllWindows()
            self.stopped = True
            self.related_video_stream.stop()
            exit(0)
