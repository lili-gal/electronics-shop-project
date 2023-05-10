import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard

@pytest.fixture
def item3():
    return Item("Смартфон", 20000, 10)


def test_calculate_total_price(item3):

    item3.calculate_total_price()
    assert item3.calculate_total_price() == 200000


def test_apply_discount(item3):
    item3.apply_discount()
    assert item3.calculate_total_price() == 200000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test__repr__():
    item1 = Item('Смартфон', 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test__str__():
    item1 = Item('Смартфон', 10000, 20)
    assert str(item1) == 'Смартфон'


def test__repr__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    kb.change_lang().change_lang()
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"