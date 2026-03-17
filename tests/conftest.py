import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки."""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "white bun"
    bun.get_price.return_value = 200.0
    return bun

@pytest.fixture
def mock_ingredient():
    """Фикстура для создания мока ингредиента."""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100.0
    ingredient.get_type.return_value = "SAUCE"
    return ingredient

@pytest.fixture
def burger():
    """Фикстура для создания объекта Бургера перед каждым тестом."""
    return Burger()