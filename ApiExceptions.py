
class ApiException(Exception):

    def __init__(self, code):
        self.code = code
        print("We got a problem! {}".format(self.code))
