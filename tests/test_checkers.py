# This is the file in which we will write our tests for the checkers module.

from verify.checkers import Checkers
import pytest

# TDD: iteration 1
# arrange
@pytest.mark.parametrize("email_address, expected_value", [
    ("john@doe.com", True),
    ("@doe.com", False),
    ("john.doe@mail.com", True),
])
def test_name_before_at_sign(email_address, expected_value):
    # act
    returned_value = Checkers.check_if_name_before_at_sign(email_address)
    # assert
    assert returned_value == expected_value
