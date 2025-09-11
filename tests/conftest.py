import sys
from pathlib import Path
from unittest.mock import Mock
import pytest


sys.path.insert(0, str(Path(__file__).parent.parent))

from praktikum.data import MOCK_BUN_NAME, MOCK_BUN_PRICE, MOCK_INGREDIENT_NAME, MOCK_INGREDIENT_PRICE, MOCK_INGREDIENT_TYPE

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = MOCK_BUN_NAME
    bun.get_price.return_value = MOCK_BUN_PRICE
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = MOCK_INGREDIENT_PRICE
    ingredient.get_name.return_value = MOCK_INGREDIENT_NAME
    ingredient.get_type.return_value = MOCK_INGREDIENT_TYPE
    return ingredient
