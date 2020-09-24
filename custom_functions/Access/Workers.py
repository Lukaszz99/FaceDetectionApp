# this class is write for testing the project
# finally Workers should be read from some database and be secured
# from unauthorized access


class Workers:
    def __init__(self):
        self.workers = ['Filip', 'Lukasz', 'Pawel', 'Sebastian']

    def get_workers(self):
        return self.workers
