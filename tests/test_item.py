"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from pathlib import Path
from src.item import Item


item = Item("a", 20.0, 2)
item2 = Item("a", 20.0, 2)

pay_rate = 0.85
short_name = "короткое"
long_name = "длинноеимяяяя"


def test_name_short():
    item.name = short_name
    assert item.name == short_name


def test_name_long():
    item.name = long_name
    assert item.name == long_name[:10]


def test_calculate_total_price():
    assert item.calculate_total_price() == 40
    assert type(item.calculate_total_price()) == float


def test_apply_discount():
    assert item.price * pay_rate == 17


def test_string_to_number():
    assert type(Item.string_to_number(item.price)) == int


def test__repr__():
    assert repr(item) == "Item('длинноеимя', 20.0, 2)"

def test__str__():
    assert str(item) == 'длинноеимя'


def test__add__():
    assert item.quantity + item2.quantity == 4


def test_errors_file_not_found():
    Item.DATA_DIR = Path(__file__).parent.joinpath('items_not.csv')
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_errors_file_broken():
    Item.DATA_DIR = Path(__file__).parent.joinpath('../src/items_broken.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()