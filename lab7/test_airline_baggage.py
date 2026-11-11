from hypothesis import given, strategies as st
from airline_baggage import parse_booking, total_weight, tag_label

@given(st.text() | st.none() | st.integers() | st.floats() | st.lists(st.text()))
def test_parse_booking_no_crash(s):
    try:
        parse_booking(s)
    except Exception as e:
        assert False, f"parse_booking crashed with input {s!r}: {e}"

@given(st.text() | st.none() | st.integers() | st.floats() | st.lists(st.text()))
def test_total_weight_no_crash(s):
    try:
        total_weight(s)
    except Exception as e:
        assert False, f"total_weight crashed with input {s!r}: {e}"

@given(st.text() | st.none() | st.integers() | st.floats() | st.lists(st.text()))
def test_tag_label_no_crash(s):
    try:
        tag_label(s)
    except Exception as e:
        assert False, f"tag_label crashed with input {s!r}: {e}"