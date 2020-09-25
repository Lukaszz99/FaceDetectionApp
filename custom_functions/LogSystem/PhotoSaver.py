import datetime
import cv2 as cv
from custom_functions.LogSystem.LogAccessesTXT import LogAccessesTXT


class PhotoSaver:
    def __init__(self):
        self.min_frames = 30
        self.frame_unknown_counter = 0
        self.frame_no_access_counter = 0

    def save_unknown_person(self, frame, video_stream):
        self.frame_unknown_counter += 1

        if self.frame_unknown_counter >= self.min_frames:
            LogAccessesTXT().log_unknown_person(video_stream)

            str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
            file_path = "log/UNKNOWN_PHOTOS/"
            file_name = file_path + str_date + '_Unknown_Person.jpeg'

            # save photo and set flag to lower quality
            cv.imwrite(file_name, frame, [cv.IMWRITE_JPEG_QUALITY, 40])
            self.frame_unknown_counter = 0

    def save_no_access_person(self, name, frame):
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
        file_path = "log/NO_ACCESS_PHOTOS/"
        file_name = file_path + str_date + '_No_Access_' + name + '.jpeg'

        # save photo and set flag to lower quality
        cv.imwrite(file_name, frame, [cv.IMWRITE_JPEG_QUALITY, 40])
        self.frame_no_access_counter = 0
