from src.item import Item


class MixinLog:
    _language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"
        else:
            self._language = "EN"


class Keyboard(Item, MixinLog):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

