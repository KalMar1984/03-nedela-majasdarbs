"""
validators.py
Satur funkcijas ievades validācijai.
"""


def validate_number(user_input):
    """
    Pārbauda vai ievade ir vesels skaitlis.
    Ja ir – atgriež int.
    Ja nav – atgriež None.
    """
    try:
        return int(user_input)
    except ValueError:
        return None


if __name__ == "__main__":
    print(validate_number("10"))   # 10
    print(validate_number("abc"))  # None