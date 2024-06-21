import pytest
from string_utils import StringUtils

# Тест #1


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize_positive(string_utils: StringUtils):

    assert string_utils.capitalize("pyton") == "Pyton"
    assert string_utils.capitalize("добрый вечер") == "Добрый вечер"
    assert string_utils.capitalize("+79991234568") == "+79991234568"


def test_capitalize_negative(string_utils: StringUtils):

    assert string_utils.capitalize("1") == "1"
    assert string_utils.capitalize(".") == "."
    assert string_utils.capitalize("交") == "交"

# Тест #2


def test_trim_positive(string_utils: StringUtils):

    assert string_utils.trim("   pyton") == "pyton"
    assert string_utils.trim("  добрый вечер") == "добрый вечер"
    assert string_utils.trim("  +79991234568") == "+79991234568"


def test_trim_negative(string_utils: StringUtils):

    assert string_utils.trim(" 交") == "交"
    assert string_utils.trim(" .") == "."
    assert string_utils.trim("1") == "1"

# Тест #3


def test_to_list_positive(string_utils: StringUtils):

    assert string_utils.to_list("p,y,t,o,n") == ["p", "y", "t", "o", "n"]
    assert string_utils.to_list("5:66:1555", ":") == ["5", "66", "1555"]
    assert string_utils.to_list("Сити,NewYork", ",") == ["Сити", "NewYork"]


def test_to_list_negative(string_utils: StringUtils):

    assert string_utils.to_list("") == []
    assert string_utils.to_list("1") == ["1"]

# Тест #4


def test_contains_positive(string_utils: StringUtils):

    assert string_utils.contains("Pyton", "P")
    assert string_utils.contains("Калининград", "л")
    assert string_utils.contains("moskow", "w")


def test_contains_negative(string_utils: StringUtils):

    assert not string_utils.contains("Pyton", "B")
    assert not string_utils.contains("Калининград", "F")
    assert not string_utils.contains("moskow", "15")

# Тест #5


def test_delete_symbol_positive(string_utils: StringUtils):

    assert string_utils.delete_symbol("Pyton", "P") == "yton"
    assert string_utils.delete_symbol("Сити", "ти") == "Си"
    assert string_utils.delete_symbol("Сити,сочи", ",") == "Ситисочи"


def test_delete_symbol_negative(string_utils: StringUtils):

    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", " ") == ""

# Тест #6


def test_starts_with_positive(string_utils: StringUtils):

    assert string_utils.starts_with("Москва", "М")
    assert not string_utils.starts_with("Москва", "k")
    assert not string_utils.starts_with("Москва", "o")


def test_starts_with_negative(string_utils: StringUtils):

    assert not string_utils.starts_with("", "U")
    assert not string_utils.starts_with(" ", " ")
    assert not string_utils.starts_with(None, "m")

# Тест #7


def test_end_with_positive(string_utils: StringUtils):

    assert string_utils.end_with("Москва", "а")
    assert not string_utils.end_with("Москва", "y")
    assert string_utils.end_with("Москва,калининград,Питер", "р")


def test_end_with_negative(string_utils: StringUtils):

    assert not string_utils.end_with("", "U")
    assert not string_utils.end_with(" ", " ")
    assert not string_utils.end_with(None, "m")

# Тест #8


def test_is_empty_positive(string_utils: StringUtils):

    assert string_utils.is_empty("")
    assert string_utils.is_empty(" ")
    assert string_utils.is_empty("  ")


def test_is_empty_negative(string_utils: StringUtils):

    assert not string_utils.is_empty("Москва")
    assert not string_utils.is_empty("+79991234568")
    assert not string_utils.is_empty("Москва,калининград,Питер")

# Тест #9


def test_list_to_string_positive(string_utils: StringUtils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"


def test_list_to_string_negative(string_utils: StringUtils):
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([], "-") == ""
    assert string_utils.list_to_string("1") == "1"
