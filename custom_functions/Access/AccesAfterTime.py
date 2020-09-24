"""
This class provide access while person is recognized for X seconds
If access is granted, it is log into log file
If access is not granted or person is Unknows screenshot is taken and this situation is also logged
"""
import time
import datetime
import cv2 as cv


class AccessAfterTime:
    def __init__(self):
        self.min_sec = 2.5
        self.min_frames = 50
        self.start_time = time.time()
        self.end_time = 0
        self.frames_read = 0
        self.access_dict = {}
        self.names = []
        self.unknown_frames_counts = 0
        self.no_access_frames_counts = 0

    def get_persons_from_frame(self, names, access, frame):
        self.names = names
        self.frames_read += 1
        for name in self.names:
            if name == 'Unknown':
                self._save_unknown_person(frame)
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
                            self._save_no_access_photo(frame)
                    else:
                        if access[name_idx][1]:
                            self.access_dict[name] = 1
                        else:
                            self.access_dict[name] = -1
                            self._save_no_access_photo(frame)

    def log_access(self, video_stream):
        if self._check_time():
            with_access, withOUT_access = self._access_after_time()
            if with_access:
                self._log_access_granted(video_stream, with_access)
            if withOUT_access:
                self._log_no_access(video_stream, withOUT_access)

    def _check_time(self):
        self.end_time = time.time()
        if self.end_time - self.start_time >= self.min_sec:
            self.start_time = time.time()
            self.end_time = 0
            return True

    def _access_after_time(self):
        persons_on_video = self.access_dict.keys()
        person_with_access = []
        person_withOUT_access = []

        for person in persons_on_video:
            person_ratio = self.access_dict[person] / self.frames_read
            if person_ratio >= 0.70:
                person_with_access.append(person)

            if person_ratio < -0.1:
                person_withOUT_access.append(person)

        # reset values
        self.frames_read = 0
        self.access_dict = {}

        return person_with_access, person_withOUT_access

    def _save_unknown_person(self, frame):
        self.unknown_frames_counts += 1

        # if Unknown person was on more than 30 frames, save it
        if self.unknown_frames_counts > self.min_frames:
            file_path = "log/UNKNOWN_PHOTOS/"
            date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
            file_name = file_path + date + '_Unknown_person.png'
            cv.imwrite(file_name, frame)
            self.unknown_frames_counts = 0

    def _save_no_access_photo(self, frame):
        self.no_access_frames_counts += 1

        if self.no_access_frames_counts > self.min_frames:
            file_path = "log/NO_ACCESS_PHOTOS/"
            date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
            file_name = file_path + date + '_no_access.png'
            cv.imwrite(file_name, frame)
            self.no_access_frames_counts = 0

    def _log_access_granted(self, video_stream, with_access):
        date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} (ID:{}) in {}, {} person with access granted! {}\n".format(
            date, video_stream.name, id(video_stream.name),
            video_stream.location, len(with_access), with_access))

        file.close()

    def _log_no_access(self, video_stream, withOUT_access):
        date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]
        file = open("log/log.txt", "a")

        file.write("{}: {} (ID:{}) in {}, {} person without access! {}\n".format(
                    date, video_stream.name, id(video_stream.name),
                    video_stream.location, len(withOUT_access), withOUT_access))

        file.close()
