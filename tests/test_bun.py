import pytest
from praktikum.bun import Bun
from praktikum.data import BUN_NAMES, BUN_PRICES

class TestBun:
    @pytest.mark.parametrize("name", BUN_NAMES)
    def test_bun_names(self, name):
        price = 99.0
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("price", BUN_PRICES)
    def test_bun_price(self, price):
        name = "black bun"
        bun = Bun(name, price)

        assert bun.get_price() == price
