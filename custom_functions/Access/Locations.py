# this class is write for testing the project
# finally Locations should be read from some database and be secured
# from unauthorized access


class Locations:
    def __init__(self):
        self.locations = ['Main_gate', 'Lab1', 'Lab2', 'Restaurant']

    def get_locations(self):
        return self.locations
