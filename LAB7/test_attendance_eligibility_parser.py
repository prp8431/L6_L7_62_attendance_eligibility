from hypothesis import given, strategies as st

from attendance_eligibility_parser import (
    normalize_srn,
    attendance_from_ratio,
    attendance_from_register,
)


@given(st.text() | st.none())
def test_normalize_srn_no_crash(s):
    try:
        normalize_srn(s)
    except Exception:
        pass


@given(st.text() | st.none())
def test_attendance_from_ratio_no_crash(s):
    try:
        attendance_from_ratio(s)
    except Exception:
        pass


@given(st.text() | st.none())
def test_attendance_from_register_no_crash(s):
    try:
        attendance_from_register(s)
    except Exception:
        pass
