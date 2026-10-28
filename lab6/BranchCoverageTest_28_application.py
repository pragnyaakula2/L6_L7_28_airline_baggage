import pytest
from airline_baggage import baggage_fee, carry_on_ok, check_in_status


def test_baggage_fee_branches():
    # Unknown cabin and negative weight
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)

    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)

    # Member condition: false, true for non-business, true for business
    assert baggage_fee("economy", 15, "domestic", False) == 0
    assert baggage_fee("economy", 25, "domestic", True) == 0
    assert baggage_fee("business", 40, "domestic", True) == 0

    # Excess <= 0 and excess > 0
    assert baggage_fee("premium", 25, "domestic", False) == 0
    assert baggage_fee("premium", 30, "domestic", False) == 100

    # Domestic and non-domestic route
    assert baggage_fee("economy", 20, "domestic", False) == 100
    assert baggage_fee("economy", 20, "international", False) == 225

    # Excess <= 20 and excess > 20
    assert baggage_fee("economy", 35, "domestic", False) == 400
    assert baggage_fee("economy", 36, "international", False) == 2100


def test_carry_on_branches():
    # Infant branch, both outcomes
    assert carry_on_ok(10, 2, True) is True
    assert carry_on_ok(10, 3, True) is False

    # Non-infant weight condition, both outcomes
    assert carry_on_ok(8, 1, False) is False
    assert carry_on_ok(7, 1, False) is True

    # Item limit, both outcomes
    assert carry_on_ok(5, 1, False) is True
    assert carry_on_ok(5, 2, False) is False


def test_check_in_status_branches():
    # Baggage cutoff: 60 vs 45
    assert check_in_status(60, True, False) == "open"
    assert check_in_status(45, False, False) == "open"

    # International cutoff adjustment: true and false
    assert check_in_status(120, True, True) == "open"
    assert check_in_status(60, True, False) == "open"

    # Open, late and closed outcomes
    assert check_in_status(60, True, False) == "open"
    assert check_in_status(50, True, False) == "late"
    assert check_in_status(44, True, False) == "closed"

    # International late and closed outcomes
    assert check_in_status(110, True, True) == "late"
    assert check_in_status(104, True, True) == "closed"
