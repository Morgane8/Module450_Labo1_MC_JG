# Here is the class in which we'll have all checking methods

import re

class Checkers:
    @staticmethod
    def check_if_name_before_at_sign(email_address):
        local_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@")
        if re.match(local_regex, email_address):
            return True
        else:
            return False