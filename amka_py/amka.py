"""
A validator for greek social security number (AMKA)
More information is available on
[AMKA.gr](https://www.amka.gr/tieinai.html).
"""

from datetime import datetime


def validate(amka: str) -> (bool, str):
    """
    Validates a greek social security number (AMKA)

    Args:
        amka (string): The string to validate

    Returns:
        (tuple): tuple containing:
            - (bool): If provided string is a valid AMKA
            - (str): Validation failure or empty
    """
    if not amka.isnumeric():
        return False, "Provided AMKA is not a numeric value"

    if len(amka) != 11:
        return False, "Provided number is not 11 digits long"

    try:
        datetime.strptime(amka[:6], "%d%m%y")
    except ValueError:
        return (
            False,
            "First 6 digits of the provided AMKA do not represent a valid date",
        )

    # Verify check digit based on Luhn algorithm
    digits = list(map(int, amka))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    checksum = (odd_sum + even_sum) % 10

    if checksum != 0:
        return False, "Provided AMKA does not have a valid checkdigit"

    return True, ""
