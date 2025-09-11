from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.data import MOCK_BUN_NAME, MOCK_INGREDIENT_NAME, MOCK_BUN_PRICE, MOCK_INGREDIENT_PRICE, MOCK_INGREDIENT_TYPE

class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.ingredients = [Mock(), mock_ingredient]
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_ingredient

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_result = burger.get_price()
        actual_result = MOCK_BUN_PRICE * 2 + MOCK_INGREDIENT_PRICE

        assert expected_result == actual_result

    def test_get_receipt(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_price = MOCK_BUN_PRICE * 2 + MOCK_INGREDIENT_PRICE
        # Учитываем тип ингредиента в ожидаемом результате
        expected_result = f'(==== {MOCK_BUN_NAME} ====)\n= {MOCK_INGREDIENT_TYPE.lower()} {MOCK_INGREDIENT_NAME} =\n(==== {MOCK_BUN_NAME} ====)\n\nPrice: {expected_price}'

        actual_result = burger.get_receipt()
        assert actual_result == expected_result
