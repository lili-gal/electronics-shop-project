import pytest
from src.item import Item


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
