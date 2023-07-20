from pages.orderpage import OrderPage
import pytest
import allure
class TestOrderPages:

    @allure.title('Заказ самоката.')
    @allure.description('Заказ самокатов через разные кнопки "Заказать" и в разных цветах.')
    @pytest.mark.parametrize('button_place, colour', [('top', 'black'), ('bottom', 'grey')])
    def test_make_order_via_up_button(self, driver_fixt, button_place, colour):

        order_page = OrderPage(driver_fixt)
        order_page.make_order(button_place, colour)

        assert "Заказ оформлен" in order_page.check_order_was_made()
        order_page.check_status_button_click()

        order_page.samokat_logo_click()
        assert "Самокат" in order_page.check_samokat_main_page()

        order_page.yandex_logo_click()
        assert True == order_page.check_yandex_main_page()