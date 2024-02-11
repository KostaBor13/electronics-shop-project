
import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def _language_test():
    with pytest.raises(AssertionError):
        kb._language = "CH"


def test_language():
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang()
    assert str(kb.language) == "EN"


