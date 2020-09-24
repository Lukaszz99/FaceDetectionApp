"""
This class provide access while person is recognized for X seconds
If access is granted, it is log into log file
If access is not granted or person is Unknows screenshot is taken and this situation is also logged
"""
import time


class AccessAfterTime:
    def __init__(self):
        self.min_sec = 2
        self.start_time = time.time()
        self.end_time = 0
        self.frames_read = 0
        self.access_dict = {}

    def get_persons_from_frame(self, names, access, frame):
        self.frames_read += 1
        for name in names:
            if name == 'Unknown':
                names.remove(name)
            else:
                for i in range(len(access)):
                    # [0] is to get first element from one-element list
                    name_idx = [x for x, y in enumerate(access) if y[0] == name][0]

                    # if person has access, add this to dict
                    if access[name_idx][1]:
                        if name in self.access_dict.keys():
                            print('a', name)
                            # if person was in dict just add +1 in name
                            self.access_dict[name] += 1
                        else:
                            print('b', name)
                            # if this person is first time on frame,
                            # add this name to dict
                            self.access_dict[name] = 1

    def log_access(self, video_stream):
        if self._check_time():
            with_access, withOUT_access = self.access_after_time()
            if with_access:
                print("{} (ID:{}) in {}, {} person with access granted! {}".format(
                    video_stream.name, id(video_stream.name),
                    video_stream.location, len(with_access), with_access))
            if withOUT_access:
                print("{} (ID:{}) in {}, {} person without access! {}".format(
                    video_stream.name, id(video_stream.name),
                    video_stream.location, len(withOUT_access), withOUT_access))

    def _check_time(self):
        self.end_time = time.time()
        if self.end_time - self.start_time >= self.min_sec:
            self.start_time = time.time()
            self.end_time = 0
            return True

    def access_after_time(self):
        persons_on_video = self.access_dict.keys()
        person_with_access = []
        person_withOUT_access = []

        for person in persons_on_video:
            print(self.access_dict[person])
            person_ratio = self.access_dict[person] / self.frames_read
            if person_ratio >= 0.85:
                person_with_access.append(person)
            if person_ratio < 0.70:
                person_withOUT_access.append(person)

            # reset values
            self.frames_read = 0
            self.access_dict = {}
        return person_with_access, person_withOUT_access
