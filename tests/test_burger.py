import pytest
from unittest.mock import Mock

class TestBurger:

    # 1. Проверка добавления булочки
    def test_add_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    # 2. Проверка добавления ингридиента
    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    # 3. Проверка удаления ингридиента
    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    # 4. Проверка перемещения ингридиентов
    @pytest.mark.parametrize("old_index, new_index", [
        (0, 1),
        (1, 0),
    ])
    def test_move_ingredient(self, burger, old_index, new_index):
        
        ing1 = Mock()
        ing2 = Mock()
        burger.ingredients = [ing1, ing2]
        
        moving_item = burger.ingredients[old_index]        
        burger.move_ingredient(old_index, new_index)

        assert burger.ingredients[new_index] == moving_item

    # 5. Проверка стоимости бургера (200*2+100=500)
    def test_get_price(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)        
        
        expected_price = (mock_bun.get_price() * 2) + mock_ingredient.get_price()

        assert burger.get_price() == expected_price

    # 6. Проверка формата чека
    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        
        receipt = burger.get_receipt()        
        
        assert f"(==== {mock_bun.get_name()} ====)" in receipt
        assert f"= {str(mock_ingredient.get_type()).lower()} {mock_ingredient.get_name()} =" in receipt
        assert f"Price: {burger.get_price()}" in receipt