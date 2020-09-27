import datetime
import cv2 as cv
from custom_functions.LogSystem.LogAccessesTXT import LogAccessesTXT


class PhotoSaver:
    """
    This class save photo of person with no access.
    """
    def __init__(self):
        self.min_frames = 30
        self.frame_unknown_counter = 0
        self.frame_no_access_counter = 0

    def save_unknown_person(self, frame, video_stream):
        """
        If unknown person was on at least 30 frames (min_frames variable in __init__)
         its photo is saved in UNKNOWN_PHOTOS folder. Also log this into log.txt file

        Args:
            frame (numpy.ndarray): photo of unknown person
            video_stream (WebCamStream): source of frame to save photo
        """
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
        """
        Save photo of person with no_access in NO_ACCESS_PHOTOS folder

        Args:
            name (str): name of person without access
            frame (numpy.ndarray): photo of unknown person
        """
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
        file_path = "log/NO_ACCESS_PHOTOS/"
        file_name = file_path + str_date + '_No_Access_' + name + '.jpeg'

        # save photo and set flag to lower quality
        cv.imwrite(file_name, frame, [cv.IMWRITE_JPEG_QUALITY, 40])
        self.frame_no_access_counter = 0
