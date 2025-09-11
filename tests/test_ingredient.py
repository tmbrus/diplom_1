import pytest
from praktikum.ingredient import Ingredient
from praktikum.data import INGREDIENT_TYPES, INGREDIENT_NAMES, INGREDIENT_PRICES

class TestIngredient:

    @pytest.mark.parametrize("types", INGREDIENT_TYPES)
    def test_ingredients_types(self, types):
        name = "hot sauce"
        price = 100.0
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_type() == types

    @pytest.mark.parametrize("name", INGREDIENT_NAMES)
    def test_ingredients_names(self, name):
        types = "SAUCE"
        price = 100.0
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", INGREDIENT_PRICES)
    def test_ingredients_price(self, price):
        types = "SAUCE"
        name = "hot sauce"
        ingredient = Ingredient(types, name, price)

        assert ingredient.get_price() == price