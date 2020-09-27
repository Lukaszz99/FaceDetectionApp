class Workers:
    """
    This class is write for testing the project. Finally Workers should be read from some database and be secured
    from unauthorized access.
    """
    def __init__(self):
        self.workers = ['Filip', 'Lukasz', 'Pawel', 'Sebastian']

    def get_workers(self):
        """

        Return:
            list of workers.
        """
        return self.workers
