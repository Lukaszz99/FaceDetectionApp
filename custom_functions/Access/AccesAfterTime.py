import time
from threading import Thread
from custom_functions.LogSystem.PhotoSaver import PhotoSaver
from custom_functions.LogSystem.LogAccessesTXT import LogAccessesTXT


class AccessAfterTime:
    """
    | This class provide access while person is recognized for X seconds
    | If access is granted, it is log into log file
    | If access is not granted or person is Unknown, screenshot is taken and this situation is also logged

    Args:
        min_time (float): minimum amount of time a person must be recognized to gain access.
    """
    def __init__(self, min_time=2.5):
        # variables for measuring time
        self.start_time = time.time()
        self.end_time = 0

        # time in sec after
        # which access is checked
        self.min_sec = min_time

        # variable to calculate person ratio
        # on frames in min_time
        # person_ratio is
        # number_of_frames_with_specific_person / frame_read
        # this variable is reset to 0 after each access checking after min_time
        self.frames_read = 0

        self.access_dict = {}
        self.names = []

        # image to keep frame of
        # last seen unknown person
        self.no_access_frame = None

        # keep access for location of related camera
        # if granted, expires after 1sec
        # False by default
        self.location_access = False

        # classes to save no_access and unknown
        # persons images and log it into lol.txt
        self.photo_saver = PhotoSaver()
        self.txt_logger = LogAccessesTXT()

    def get_persons_from_frame(self, names, access, frame, video_stream):
        """
        If person is recognized on frame add this name to dict, where all names are kept. If person has
        access add +1 in this name. If person don't have access add -1 in this name. Names with negative value
        of person_ratio (access_after_time method) are recognized as persons without access.

        Args:
            names (list): list of names people on frame. Can contain 'Unknown' if person is not in known persons .pickle file.
            access (list): list of tuples (Name, Access(True/False)). Used to measure person_ratio.
            frame (numpy.ndarray): last frame with unknown or person with no access.
            video_stream (WebCamStream): source of video.
        """
        self.names = names
        self.frames_read += 1
        for name in self.names:
            if name == 'Unknown':
                self.photo_saver.save_unknown_person(frame, video_stream)
                self.names.remove(name)
            else:
                for i in range(len(access)):
                    # [0] is to get first element from one-element list
                    name_idx = [x for x, y in enumerate(access) if y[0] == name][0]

                    if name in self.access_dict.keys():
                        if access[name_idx][1]:
                            self.access_dict[name] += 1
                        else:
                            self.access_dict[name] -= 1
                            self.no_access_frame = frame
                    else:
                        if access[name_idx][1]:
                            self.access_dict[name] = 1
                        else:
                            self.access_dict[name] = -1
                            self.no_access_frame = frame

    def log_access(self, video_stream):
        """
        If min_time passed, save into log.txt file who get access or not. Also save from video stream
        for person without access or unknown person. If someone get access location_access variable.
        is set to True. After 1sec is set to False.

        Args:
            video_stream (WebCamStream): source of video.
        """
        if self.check_time():
            with_access, withOUT_access = self.access_after_time()
            if with_access:
                self.txt_logger.log_access_granted(video_stream, with_access)
                self._set_access_in_location()
            if withOUT_access:
                self.txt_logger.log_no_access(video_stream, withOUT_access)
                self.photo_saver.save_no_access_person(withOUT_access[0], self.no_access_frame)

    def access_in_location(self):
        """
        Return:
            True if access is grant in given location
        """
        return self.location_access

    def _set_access_in_location(self):
        """set access to True, after 1sec set to False."""
        self.location_access = True

        # make thread to set access to False
        # after 1 sec
        thread = Thread(target=self._set_False)
        thread.start()

    def _set_False(self):
        time.sleep(1)
        self.location_access = False

    def check_time(self):
        """
        Return:
            True if min_time passed.
        """
        self.end_time = time.time()
        if self.end_time - self.start_time >= self.min_sec:
            self.start_time = time.time()
            self.end_time = 0
            return True

    def access_after_time(self):
        """
        Calculate person ratio in last min_time period. Ratio =
        score from get_persons_from_frame / frames read in min_time period.

        Return:
            2 list of persons, with access and without access.
        """
        persons_on_video = self.access_dict.keys()
        person_with_access = []
        person_withOUT_access = []

        for person in persons_on_video:
            person_ratio = self.access_dict[person] / self.frames_read
            if person_ratio >= 0.85:
                person_with_access.append(person)

            if person_ratio < -0.85:
                person_withOUT_access.append(person)

        # reset values
        self.frames_read = 0
        self.access_dict = {}

        return person_with_access, person_withOUT_access
