import pandas as pd
from .Workers import Workers
from .Locations import Locations


class AccessLevel:
    def __init__(self):
        self.workers = Workers().get_workers()
        self.locations = Locations().get_locations()
        self.names = []
        # set all accesses to False by default
        self.access = {key: [False for _ in range(len(self.workers))] for key in self.locations}
        self.access_frame = pd.DataFrame(self.access, index=self.workers)

    def add_access_everywhere_by_name(self, name):
        self.access_frame.at[name, self.locations] = True

    def add_access_in_location_by_name(self, name, location):
        self.access_frame.at[name, location] = True

    def remove_access_everywhere_by_name(self, name):
        self.access_frame.at[name, self.locations] = False

    def remove_access_in_location_by_name(self, name, location):
        self.access_frame.at[name, location] = False

    def get_access(self, names, location):
        self.names = names
        if not self.names:
            return False
        else:
            if location not in self.locations:
                print("{} is not recognize as any camera's location. Location should be on of this: \n {}"
                      .format(location, self.locations))
                return False
            else:
                if 'Unknown' in self.names:
                    self.names.remove('Unknown')
                access = [(name, self.access_frame.loc[name][location]) for name in self.names]
                return list(access)

    def who_on_video(self, video_stream):
        # return camera name, unique id of cam object, location of camera, number of persons on frame and their names
        return video_stream.name, id(video_stream), video_stream.location, len(self.names), self.names

    def set_custom_accesses(self):
        # this function is only for checking program
        # in final version access should be given by admin
        # or read from database
        self.add_access_everywhere_by_name('Filip')
        self.add_access_everywhere_by_name('Lukasz')
        self.add_access_in_location_by_name('Pawel', ['Main_gate', 'Lab2'])
        self.add_access_in_location_by_name('Sebastian', ['Main_gate', 'Lab2'])
