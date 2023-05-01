import self as self
import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)

    @property
    def name(self):
        return self.__name

    # noinspection PyPropertyDefinition
    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value
        else:
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):

        with open("C:/Users/User/PycharmProjects/electronics-shop-project/src/items.csv",  encoding='windows-1251') as file:
            file_reader = csv.DictReader(file)
            for row in file_reader:
                item = cls(row['name'], cls.string_to_number(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(value):
        return int(float(value))
