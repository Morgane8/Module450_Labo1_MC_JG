# Here is the class in which we'll have all checking methods

import re

# Define regex for local part before the '@'
LOCAL_PART_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@")

class Checkers:
    @staticmethod
    def check_if_name_before_at_sign(email_address):
        return bool(LOCAL_PART_REGEX.match(email_address))