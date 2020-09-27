class Locations:
    """
    This class is write for testing the project. Finally Locations should be read from some database
     and be secured from unauthorized access.

    """
    def __init__(self):
        self.locations = ['Main_gate', 'Lab1', 'Lab2', 'Restaurant']

    def get_locations(self):
        """

        Return:
            list of locations.
        """
        return self.locations
