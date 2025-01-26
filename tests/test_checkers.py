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

# TDD: iteration 2
# arrange
@pytest.mark.parametrize("email_address, expected_value", [
    ("john@doe.com", True),
    ("john.doe.com", False),
    ("john@doe@test.com", False),
])
def test_if_there_is_one_at_sign(email_address, expected_value):
    # act
    returned_value = Checkers.check_if_there_is_one_at_sign(email_address)
    # assert
    assert returned_value == expected_value

    # TDD: iteration 3
# arrange
@pytest.mark.parametrize("email_address, expected_value", [
    ("john@doe.com", True),
    ("john@doe", False),
    ("john@.com", False),
])
def test_if_there_is_a_domain_name(email_address, expected_value):
    # act
    returned_value = Checkers.check_for_domain_name(email_address)
    # assert
    assert returned_value == expected_value