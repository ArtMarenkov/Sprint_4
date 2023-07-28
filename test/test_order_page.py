from pages.order_page import OrderPage
import pytest
import allure

class TestOrderPages:

    @allure.title('Заказ самоката.')
    @allure.description('Заказ самокатов через разные кнопки "Заказать" и в разных цветах.')
    @pytest.mark.parametrize('button_place, colour', [('top', 'black'), ('bottom', 'grey')])
    def test_make_order_via_up_button(self, driver_fixt, button_place, colour):
        order_page = OrderPage(driver_fixt)
        order_page.make_order(button_place, colour)
        assert "Заказ оформлен" in order_page.check_order_was_made(), "Заказ не оформлен."

    @allure.title('Переход на главную страницу "Самоката" после заказа.')
    @allure.description('После заказа самоката кликаем на логотип "Самокат" и переходим на главную страницу')
    def test_main_page_transition_after_order(self, driver_fixt):
        order_page = OrderPage(driver_fixt)
        order_page.make_order('top', 'grey')
        order_page.check_status_button_click()
        order_page.samokat_logo_click()
        assert "Самокат" in order_page.check_samokat_main_page(), "Переход на главную страницу 'Самоката' не осуществлён."

    @allure.title('Переход на главную страницу "Дзена" из "Самоката".')
    @allure.description('Переход на главную страницу "Дзена" с главной страницы заказа самокатов.')
    def test_dzen_page_transition_after_order(self, driver_fixt):
        order_page = OrderPage(driver_fixt)
        order_page.make_order('bottom', 'black')
        order_page.check_status_button_click()
        order_page.samokat_logo_click()
        order_page.yandex_logo_click()
        assert True == order_page.check_yandex_main_page(), "Переход на главную страницу 'Дзен' не осуществлён."