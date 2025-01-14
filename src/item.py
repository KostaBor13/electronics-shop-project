import csv
import os
from pathlib import Path


class InstantiateCSVError(KeyError):
    def __str__(self):
        return "Файл поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    DATA_DIR = Path(__file__).parent.joinpath('items.csv')

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
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        all_price = self.price * self.quantity
        return all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name = value[:10]
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        try:
            with cls.DATA_DIR.open(newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all.clear()
                try:
                    for row in reader:
                        name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        cls(name, price, quantity)
                except KeyError:
                    raise InstantiateCSVError(f'Файл items.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл items.csv')
        else:
            return cls


    @staticmethod
    def string_to_number(value: str) -> float:
        """Преобразует строку с числом в число."""
        return int(float(value))