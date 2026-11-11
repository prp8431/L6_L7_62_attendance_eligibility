def normalize_srn(srn):
    """
    Trims and upper-cases a student registration number.
    Handles invalid input without crashing.
    """
    try:
        if not isinstance(srn, str):
            return ""
        return srn.strip().replace(" ", "").upper()
    except Exception:
        return ""


def attendance_from_ratio(text):
    """
    Converts 'ATTENDED/HELD' into a whole-number percentage.
    Handles invalid input without crashing.
    """
    try:
        if not isinstance(text, str):
            return 0

        attended, held = text.split('/')

        attended = int(attended.strip())
        held = int(held.strip())

        if held == 0:
            return 0

        return attended * 100 // held
    except (ValueError, TypeError, ZeroDivisionError):
        return 0


def attendance_from_register(marks):
    """
    Calculates attendance percentage from P (present) and A (absent).
    Handles invalid input without crashing.
    """
    try:
        if not isinstance(marks, str):
            return 0

        marks = marks.strip().upper()

        if not marks:
            return 0

        return marks.count('P') * 100 // len(marks)
    except Exception:
        return 0


def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input(
        "Enter classes attended and held as ATTENDED/HELD (e.g. 30/40): "
    )
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter the register as P/A marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))


if __name__ == "__main__":
    main()
