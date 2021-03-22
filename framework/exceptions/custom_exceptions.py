from enum import Enum


class ResponseCodes(Enum):
    ok_code = 200
    bad_request = 400
    not_found = 404


class IncorrectStatusCodeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'IncorrectStatusCodeError, {0} '.format(self.message)
        else:
            return 'IncorrectStatusCodeError has been raised'
