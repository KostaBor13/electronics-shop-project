from src.item import Item


class Phone(Item):
    """Класс для наследования."""
    def __init__(self, name: str, price: float, quantity: int, sim_card):
        super().__init__(name, price, quantity)
        self._number_of_sim = sim_card

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        """Возврат кол.сим карт."""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Проверка условия значения на 0 и целое число"""
        if not isinstance(value, int) or value == 0:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self._number_of_sim = value