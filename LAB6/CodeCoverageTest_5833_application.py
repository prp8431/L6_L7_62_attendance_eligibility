
import pytest

from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)


# Attendance percentage tests
def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75


def test_invalid_total():
    with pytest.raises(ValueError):
        attendance_percent(10, 0, 0)


def test_negative_attendance():
    with pytest.raises(ValueError):
        attendance_percent(-1, 40, 0)


def test_attendance_more_than_total():
    with pytest.raises(ValueError):
        attendance_percent(41, 40, 0)


def test_medical_leave_limit():
    assert attendance_percent(30, 40, 7) == 87


def test_credited_attendance_limit():
    assert attendance_percent(38, 40, 5) == 100


# Exam eligibility tests
def test_fees_pending():
    assert exam_eligibility(80, False, False) == "fees pending"


def test_exam_eligible():
    assert exam_eligibility(80, False, True) == "eligible"


def test_condonation_eligible():
    assert exam_eligibility(65, True, True) == "eligible"


def test_condonation_required():
    assert exam_eligibility(65, False, True) == "condonation required"


def test_exam_detained():
    assert exam_eligibility(60, True, True) == "detained"


# Attendance warning tests
def test_no_warning():
    assert attendance_warning(90, 2) is None


def test_critical_warning():
    assert attendance_warning(70, 6) == "critical"


def test_final_notice():
    assert attendance_warning(70, 3) == "final notice"


def test_attendance_reminder():
    assert attendance_warning(80, 3) == "reminder"
