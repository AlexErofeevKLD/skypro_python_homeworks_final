import pytest
from string_utils import StringUtils

# Тест #1 Принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("pyton") == "Pyton"
    assert string_utils.capitalize("добрый вечер") == "Добрый вечер"
    assert string_utils.capitalize("+79991234568") == "+79991234568"

def test_capitalize_negative(string_utils):
    assert string_utils.capitalize(None) == None
    assert string_utils.capitalize(".") == "."
    assert string_utils.capitalize("交") == "交"

# Тест #2 Принимает на вход текст и удаляет пробелы в начале, если они есть
@pytest.fixture
def string_utils():
    return StringUtils()

def test_trim_positive(string_utils):
    assert string_utils.trim("   pyton") == "pyton"
    assert string_utils.trim("  добрый вечер") == "добрый вечер"
    assert string_utils.trim("  +79991234568") == "+79991234568"

def test_trim_negative(string_utils):
    assert string_utils.trim(" 交") == "交"
    assert string_utils.trim(" .") == "."
    assert string_utils.trim(None) == None

# Тест #3 Принимает на вход текст с разделителем и возвращает список строк. \n
@pytest.fixture
def string_utils():
    return StringUtils()

def test_to_list_positive(string_utils):
    assert string_utils.to_list("p,y,t,o,n") == ["p", "y", "t", "o", "n"]
    assert string_utils.to_list("5:66:1555", ":") == ["5", "66", "1555"]
    assert string_utils.to_list("калининград,moskow,питер", ",") == ["калининград", "moskow", "питер"]

def test_to_list_negative(string_utils):
    assert string_utils.to_list("") == []
    assert string_utils.to_list(None) == []

# Тест #4 Возвращает `True`, если строка содержит искомый символ и `False` - если нет \n
@pytest.fixture
def string_utils():
    return StringUtils()

def test_contains_positive(string_utils):
    assert string_utils.contains("Pyton", "P") == True
    assert string_utils.contains("Калининград", "л") == True
    assert string_utils.contains("moskow", "w") == True

def test_contains_negative(string_utils):
    assert string_utils.contains("Pyton", "B") == False
    assert string_utils.contains("Калининград", "F") == False
    assert string_utils.contains("moskow", "15") == False

# Тест #5 Удаляет все подстроки из переданной строки \n
@pytest.fixture
def string_utils():
    return StringUtils()

def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("Pyton", "P") == "yton"
    assert string_utils.delete_symbol("Калининград", "град") == "Калинин"
    assert string_utils.delete_symbol("Москва,калининград,Питер", ",") == "МосквакалининградПитер"

def test_delete_symbol_negative(string_utils):
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", " ") == ""
    assert string_utils.delete_symbol(None, "2") == None

# Тест #6 Возвращает `True`, если строка начинается с заданного символа и `False` - если нет \n
@pytest.fixture
def string_utils():
    return StringUtils()

def test_starts_with_positive(string_utils):
    assert string_utils.starts_with("Москва", "М") == True
    assert string_utils.starts_with("Москва", "k") == False
    assert string_utils.starts_with("Москва", "o") == False

def test_starts_with_negative(string_utils):
    assert string_utils.starts_with("", "U") == False
    assert string_utils.starts_with(" ", " ") == False
    assert string_utils.starts_with(None, "m") == False

# Тест #7 Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет \n
@pytest.fixture
def string_utils():
    return StringUtils()

def test_end_with_positive(string_utils):
    assert string_utils.end_with("Москва", "а") == True
    assert string_utils.end_with("Москва", "y") == False
    assert string_utils.end_with("Москва,калининград,Питер", "р") == True

def test_end_with_negative(string_utils):
    assert string_utils.end_with("", "U") == False
    assert string_utils.end_with(" ", " ") == False
    assert string_utils.end_with(None, "m") == False

# Тест #8 Возвращает `True`, если строка пустая и `False` - если нет \n 
@pytest.fixture
def string_utils():
    return StringUtils()

def test_is_empty_positive(string_utils):
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty(" ") == True
    assert string_utils.is_empty("  ") == True

def test_is_empty_negative(string_utils):
    assert string_utils.is_empty("Москва") == False
    assert string_utils.is_empty("+79991234568") == False
    assert string_utils.is_empty("Москва,калининград,Питер") == False

# Тест #9 Преобразует список элементов в строку с указанным разделителем \n 
@pytest.fixture
def string_utils():
    return StringUtils()

def test_list_to_string_positive(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

def test_list_to_string_negative(string_utils):
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([], "-") == ""
    assert string_utils.list_to_string(None) == ""