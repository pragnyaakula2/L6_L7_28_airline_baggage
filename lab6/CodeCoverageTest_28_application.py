import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


def test_baggage_fee_valid_cases():
    assert baggage_fee("economy", 10, "domestic", False) == 0
    assert baggage_fee("economy", 20, "domestic", False) == 100
    assert baggage_fee("premium", 30, "international", True) == 0
    assert baggage_fee("business", 45, "domestic", True) == 100
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_baggage_fee_invalid_cases():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)

    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_carry_on_cases():
    assert carry_on_ok(5, 1, False) is True
    assert carry_on_ok(8, 1, False) is False
    assert carry_on_ok(8, 2, True) is True
    assert carry_on_ok(8, 3, True) is False
    assert carry_on_ok(7, 1, False) is True
    assert carry_on_ok(5, 2, False) is False


def test_check_in_status_cases():
    assert check_in_status(60, True, False) == "open"
    assert check_in_status(50, True, False) == "late"
    assert check_in_status(40, True, False) == "closed"
    assert check_in_status(120, True, True) == "open"
    assert check_in_status(110, True, True) == "late"
    assert check_in_status(100, True, True) == "closed"
    assert check_in_status(45, False, False) == "open"
    assert check_in_status(30, False, False) == "late"
    assert check_in_status(20, False, False) == "closed"
