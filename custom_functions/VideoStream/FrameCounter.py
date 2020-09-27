import time


class FrameCounter:
    """
    This class contain number of read frames to calculate actual FPS. Read frames are set to 0 after calculating FPS
    """
    def __init__(self):
        self.frames_to_count = 20
        self.frames_read_counter = 0
        self.FPS = 0
        self.start_time = time.time()
        self.end_time = 0

    def frame_read(self):
        """Increment read frames by 1 while frame is read"""
        self.frames_read_counter += 1

    def reset_frame_read(self):
        """Reset read frames, set to 0"""
        self.frames_read_counter = 0

    def calculate_FPS(self):
        """When minimum frames are read (minimum is set in class __init__ to 20),
        they are divided by time passed since the last FPS count."""
        if self.frames_read_counter >= self.frames_to_count:

            # calculate time taken to calculate frames_to_count
            self.end_time = time.time()
            seconds = self.end_time - self.start_time

            # calculate FPS
            self.FPS = self.frames_read_counter / seconds

            # set counter to 0, to count frames from beginning
            self.frames_read_counter = 0

            # set new start time
            self.start_time = time.time()

    def get_FPS(self):
        """
        Return:
            FPS in video stream
        """
        return float("{:.2f}".format(self.FPS))
