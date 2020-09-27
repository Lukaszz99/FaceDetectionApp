import pandas as pd
from .Workers import Workers
from .Locations import Locations


class AccessLevel:
    """
    This class is checking access of persons on each frame. While initialize, this class read list
     of persons (workers) and locations from Workers.py and Location.py
    """
    def __init__(self):
        # in final version of project
        # workers and locations
        # should be loaded from database
        # or other secured place
        self.workers = Workers().get_workers()
        self.locations = Locations().get_locations()

        # set all accesses to False by default
        self.access = {key: [False for _ in range(len(self.workers))] for key in self.locations}

        # Pandas DataFrame to kep access in location per person
        self.access_frame = pd.DataFrame(self.access, index=self.workers)

        # list of names used in get_access functions
        self.names = []

    def add_access_everywhere_by_name(self, name):
        """
        Add access to every location for specific person

        Args:
            name (str): person to grant access
        """
        self.access_frame.at[name, self.locations] = True

    def add_access_in_location_by_name(self, name, location):
        """
        Add access to specific location for specific person

        Args:
            location (str or list): location where person will get access
            name (str): person to grant access
        """
        self.access_frame.at[name, location] = True

    def remove_access_everywhere_by_name(self, name):
        """
        Remove access from every location for specific person

        Args:
            name (str): person to grant access
        """
        self.access_frame.at[name, self.locations] = False

    def remove_access_in_location_by_name(self, name, location):
        """
        Remove access from specific location for specific person

        Args:
            location (str or list): location where person will get access
            name (str): person to grant access
        """
        self.access_frame.at[name, location] = False

    def get_access(self, names, location):
        """
        Check if persons on frame have access to specific location

        Args:
            names (str): person to grant access
            location (str or list): location where person will get access

        Return:
            list of tuples with persons and access [(Name, Access(True/False))]
        """
        self.names = names

        # if list of names is empty access is not grant
        if not self.names:
            return False
        else:
            if location not in self.locations:
                print("{} is not recognize as any camera's location. Location should be on of this: \n {}"
                      .format(location, self.locations))
                return False
            else:
                access = [(name, self.access_frame.loc[name][location]) for name in self.names if name != 'Unknown']
                return list(access)

    def who_on_video(self, video_stream):
        """

        Return:
             camera name, unique id of cam object, location of camera, number of persons on frame and their names
        """
        return video_stream.name, id(video_stream), video_stream.location, len(self.names), self.names

    def set_custom_accesses(self):
        """
        Use functions to add access for persons. This function is only for checking program. In final version, access should be given by admin
        or read from database
        """
        self.add_access_everywhere_by_name('Filip')
        self.add_access_everywhere_by_name('Lukasz')
        self.add_access_in_location_by_name('Pawel', ['Main_gate', 'Lab2'])
        self.add_access_in_location_by_name('Sebastian', ['Main_gate', 'Lab2'])
