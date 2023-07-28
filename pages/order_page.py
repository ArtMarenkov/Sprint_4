from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from data.locators import Locators
import allure

class OrderPage(Base_page):

    @allure.step('Нажимаем на верхнюю кнопку "Заказать".')
    def go_to_order_page_up(self):
        Base_page.wait_for_element_is_clickable(self, By.XPATH, Locators.up_order_button)
        Base_page.click_on_element(self, By.XPATH, Locators.up_order_button)

    @allure.step('Прокручиваем страницу вниз.')
    def scroll_page_down_to_order_button(self):
        Base_page.scroll_to_element(self, By.XPATH, Locators.order_button)

    @allure.step('Нажимаем на нижнюю кнопку "Заказать".')
    def go_to_order_page_bottom(self):
        Base_page.wait_for_element_is_clickable(self, By.XPATH, Locators.order_button)
        Base_page.click_on_element(self, By.XPATH, Locators.order_button)

    @allure.step('Заполняем поле "Имя".')
    def set_name(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.name_field)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.name_field, "Тестер")

    @allure.step('Заполняем поле "Фамилия".')
    def set_surname(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.surname_field)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.surname_field, "Тестеров")

    @allure.step('Заполняем поле "Адрес".')
    def set_adress(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.adress_field)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.adress_field, "Адрес")

    @allure.step('Выбираем станцию метро.')
    def set_undgrnd(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.undgrnd_station_field)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.undgrnd_station_field, Keys.DOWN)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.undgrnd_station_field, Keys.ENTER)

    @allure.step('Заполняем поле "Номер телефона".')
    def set_phone(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.phonenum_field)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.phonenum_field, "+79999999999")

    @allure.step('Переходим ко следующей форме оформления заказа.')
    def click_next_button(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.next_button)
        Base_page.click_on_element(self, By.CSS_SELECTOR, Locators.next_button)

    @allure.step('Выбираем дату доставки.')
    def set_date(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.date)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.date, "03.09.2023")
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.date, Keys.ENTER)

    @allure.step('Выбираем срок аренды.')
    def set_term(self, term_text):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.term_field)
        Base_page.click_on_element(self, By.CSS_SELECTOR, Locators.term_field)
        list_terms = Base_page.get_elements(self, By.CSS_SELECTOR, Locators.term)
        for item in list_terms:
            if item.text == term_text:
                item.click()
                break

    @allure.step('Выбираем цвет.')
    def set_colour(self, colour):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, "[id= '" + colour + "']")
        Base_page.click_on_element(self, By.CSS_SELECTOR, "[id= '" + colour + "']")

    @allure.step('Заполняем поле "Комментарий".')
    def set_comment(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.comment)
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.comment, "Комментарий")
        Base_page.send_keys_to_element(self, By.CSS_SELECTOR, Locators.comment, Keys.ENTER)

    @allure.step('Нажимаем на кнопку "Заказать".')
    def make_order_fin_click(self):
        Base_page.wait_for_element_is_clickable(self, By.XPATH, Locators.order_button)
        Base_page.click_on_element(self, By.XPATH, Locators.order_button)

    @allure.step('Подтверждаем оформление заказа.')
    def order_confirmation_click(self):
        Base_page.wait_for_element_is_clickable(self, By.XPATH, Locators.order_confirmation_button)
        Base_page.click_on_element(self, By.XPATH, Locators.order_confirmation_button)

    @allure.step('Проверяем, что заказ оформлен.')
    def check_order_was_made(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.order_made)
        return Base_page.get_element_text(self, By.CSS_SELECTOR, Locators.order_made)

    def check_status_button_click(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.check_status_button)
        Base_page.click_on_element(self, By.CSS_SELECTOR, Locators.check_status_button)

    @allure.step('Переходим на главную страницу, кликнув по лого "Самокат".')
    def samokat_logo_click(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.samokat_logo)
        Base_page.click_on_element(self, By.CSS_SELECTOR, Locators.samokat_logo)

    @allure.step('Проверяем, что перешли на главную страницу "Самокат".')
    def check_samokat_main_page(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.samokat_main_page)
        return Base_page.get_element_text(self, By.CSS_SELECTOR, Locators.samokat_main_page)

    @allure.step('Переходим на главную страницу Дзена, кликнув по лого "Яндекс".')
    def yandex_logo_click(self):
        Base_page.wait_for_element_is_clickable(self, By.CSS_SELECTOR, Locators.yandex_logo)
        Base_page.click_on_element(self, By.CSS_SELECTOR, Locators.yandex_logo)

    @allure.step('Проверяем, что перешли на главную страницу "Дзен".')
    def check_yandex_main_page(self):
        Base_page.switch_to_last_tab(self)
        Base_page.check_page_url(self, "https://dzen.ru/?yredirect=true")
        return Base_page.is_element_displayed(self, By.CSS_SELECTOR, Locators.dzen_main_page)

    def make_order(self, button_place, colour):
        if button_place == 'top':
            self.go_to_order_page_up()
        if button_place == 'bottom':
            self.scroll_page_down_to_order_button()
            self.go_to_order_page_bottom()
        self.set_name()
        self.set_surname()
        self.set_adress()
        self.set_undgrnd()
        self.set_phone()
        self.click_next_button()
        self.set_date()
        self.set_term('двое суток')
        self.set_colour(colour)
        self.set_comment()
        self.make_order_fin_click()
        self.order_confirmation_click()