
class Error(Exception):
    pass


class NoTextPartFound(Error):
    def __init__(self, message):
        self.message = message

class EmptyEmail(Error):
    def __init__(self, message):
        self.message = message