import datetime


class LogAccessesTXT:
    """
    Class for logging to txt file every time if access was granted or not. Also make a log if unknown
    person was found on video
    """
    def log_access_granted(self, video_stream, with_access):
        """
        Opens log.txt file and save info about granted access - date, camera name, location and person name

        Args:
            video_stream (WebCamStream): log info camera
            with_access (str or list): list of persons with access granted
        """
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {}, {} person with access granted! {}\n".format(
            str_date, video_stream.name,
            video_stream.location, len(with_access), with_access))

        file.close()

    def log_no_access(self, video_stream, withOUT_access):
        """
        Opens log.txt file and save info about no granted access - date, camera name, location and person name

        Args:
            video_stream (WebCamStream): log info camera
            withOUT_access (str or list): list of persons without access granted
        """
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {}, {} person without access! {}\n".format(
            str_date, video_stream.name,
            video_stream.location, len(withOUT_access), withOUT_access))

        file.close()

    def log_unknown_person(self, video_stream):
        """
        Opens log.txt file and save info about unknown person - date, camera name, location

        Args:
            video_stream (WebCamStream): log info camera
        """
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {} found UNKNOWN person!\n".format(
            str_date, video_stream.name, video_stream.location))

        file.close()
