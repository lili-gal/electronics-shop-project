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
