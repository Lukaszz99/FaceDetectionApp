import time


class FrameCounter:
    def __init__(self):
        self.frames_to_count = 15
        self.frames_readed_counter = 0
        self.FPS = 0
        self.start_time = time.time()
        self.end_time = 0

    def frame_readed(self):
        self.frames_readed_counter += 1

    def calculate_FPS(self):
        if self.frames_readed_counter >= self.frames_to_count:

            # calculate time taken to calculate frames_to_count
            self.end_time = time.time()
            seconds = self.end_time - self.start_time

            # calculate FPS
            self.FPS = self.frames_readed_counter / seconds

            # set counter to 0, to count frames from beginign
            self.frames_readed_counter = 0

            # set new start time
            self.start_time = time.time()

    def get_FPS(self):
        return self.FPS
