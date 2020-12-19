from amka_py.amka import validate


def test_it_validates_valid_amka():
    is_valid, _err = validate("09095986684")
    assert is_valid is True


def test_it_fails_when_not_a_number():
    is_valid, _err = validate("asvs")
    assert is_valid is False


def test_it_fails_when_short_number():
    is_valid, _err = validate("09095986")
    assert is_valid is False


def test_it_fails_when_long_number():
    is_valid, _err = validate("090959866845")
    assert is_valid is False


def test_it_fails_when_not_a_valid_date():
    is_valid, _err = validate("39095986681")
    assert is_valid is False


def test_it_fails_with_bad_check_digit():
    is_valid, _err = validate("09095986680")
    assert is_valid is False
