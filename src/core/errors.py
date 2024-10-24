
from core.messages import ANOTHER_TYPE_FOR_INT, NUMBER_IS_BIGGER_OR_LOWER_THAN_TYPE



class NotIntError(Exception):
    def __init__(self, message=ANOTHER_TYPE_FOR_INT):
        self.message = message
        super().__init__(self.message)


class BiggerOrLowerNumberError(Exception):
    def __init__(self, message=NUMBER_IS_BIGGER_OR_LOWER_THAN_TYPE):
        self.message = message
        super().__init__(self.message)