import datetime


class LogAccessesTXT:
    def log_access_granted(self, video_stream, with_access):
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {}, {} person with access granted! {}\n".format(
            str_date, video_stream.name,
            video_stream.location, len(with_access), with_access))

        file.close()

    def log_no_access(self, video_stream, withOUT_access):
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {}, {} person without access! {}\n".format(
            str_date, video_stream.name,
            video_stream.location, len(withOUT_access), withOUT_access))

        file.close()

    def log_unknown_person(self, video_stream):
        str_date = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")[:19]

        file = open("log/log.txt", "a")

        file.write("{}: {} in {} found UNKNOWN person!\n".format(
            str_date, video_stream.name, video_stream.location))

        file.close()
