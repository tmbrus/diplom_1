from unittest.mock import patch, Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from praktikum.data import MOCK_BUN_NAME, MOCK_BUN_PRICE

class TestDatabase:
    @patch.object(Database, 'available_buns')
    def test_available_buns(self, mock_available_buns):
        mock_bun = Mock(get_name=Mock(return_value=MOCK_BUN_NAME),
                        get_price=Mock(return_value=MOCK_BUN_PRICE))
        mock_available_buns.return_value = [mock_bun]

        db = Database()
        result = db.available_buns()

        assert result[0].get_name() == MOCK_BUN_NAME
        assert result[0].get_price() == MOCK_BUN_PRICE

    @patch.object(Database, 'available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        mock_ingredient = Mock(get_type=Mock(return_value=INGREDIENT_TYPE_SAUCE),
                               get_name=Mock(return_value="hot sauce"))
        mock_available_ingredients.return_value = [mock_ingredient]

        db = Database()
        result = db.available_ingredients()

        assert result[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert result[0].get_name() == "hot sauce"