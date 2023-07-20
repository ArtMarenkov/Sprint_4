from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure

class OrderPage:

    up_order_button = "[class *= 'Header_Nav'] [class *= 'Button']"
    bottom_order_button = "[class *= 'Finish'] [class *= 'Button']"
    name_field = "[placeholder = '* Имя']"
    surname_field = "[placeholder = '* Фамилия']"
    adress_field = "[placeholder = '* Адрес: куда привезти заказ']"
    undgrnd_station_field = "[placeholder = '* Станция метро']"
    phonenum_field = "[placeholder = '* Телефон: на него позвонит курьер']"
    next_button = "[class *= 'Order_NextButton'] button"
    date = "[placeholder = '* Когда привезти самокат']"
    term_field = "[class = 'Dropdown-placeholder']"
    term = "[class = 'Dropdown-option']"
    colour_black = "[id = 'black']"
    colour_grey = "[id = 'grey']"
    comment = "[placeholder = 'Комментарий для курьера']"
    make_an_order_button = "[class *= 'Button'] [class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    order_confirmation_button = "[class = 'Order_Modal__YZ-d3'] [class = 'Order_Buttons__1xGrp'] [class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    order_made = "[class *= 'Order_ModalHeader']"
    check_status_button = "[class *= 'Order_NextButton'] button"
    samokat_logo = "[class *= 'Header_LogoScooter']"
    samokat_main_page = "[class *= 'Home_Header']"
    yandex_logo = "[href = '//yandex.ru']"
    dzen_main_page = "[class *= 'dzen']"

    @allure.step('Открываем страницу в браузере')
    def __init__(self, driver_fixt):
        self.driver = driver_fixt

    @allure.step('Нажимаем на верхнюю кнопку "Заказать".')
    def go_to_order_page_up(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.up_order_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.up_order_button).click()

    @allure.step('Прокручиваем страницу вниз.')
    def scroll_page_down(self):
        # q_first = self.driver.find_element(By.ID, 'accordion__heading-0')
        q_first = self.driver.find_element(By.CSS_SELECTOR, self.bottom_order_button)
        self.driver.execute_script('arguments[0].scrollIntoView();', q_first)

    @allure.step('Нажимаем на нижнюю кнопку "Заказать".')
    def go_to_order_page_bottom(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.bottom_order_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.bottom_order_button).click()

    @allure.step('Заполняем поле "Имя".')
    def set_name(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.name_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.name_field).click()
        self.driver.find_element(By.CSS_SELECTOR, self.name_field).send_keys("Тестер")

    @allure.step('Заполняем поле "Фамилия".')
    def set_surname(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.surname_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.surname_field).click()
        self.driver.find_element(By.CSS_SELECTOR, self.surname_field).send_keys("Тестеров")

    @allure.step('Заполняем поле "Адрес".')
    def set_adress(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.adress_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.adress_field).click()
        self.driver.find_element(By.CSS_SELECTOR, self.adress_field).send_keys("Адрес")

    @allure.step('Выбираем станцию метро.')
    def set_undgrnd(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.undgrnd_station_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.undgrnd_station_field).click()
        self.driver.find_element(By.CSS_SELECTOR, self.undgrnd_station_field).send_keys(Keys.DOWN)
        self.driver.find_element(By.CSS_SELECTOR, self.undgrnd_station_field).send_keys(Keys.ENTER)

    @allure.step('Заполняем поле "Номер телефона".')
    def set_phone(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.phonenum_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.phonenum_field).click()
        self.driver.find_element(By.CSS_SELECTOR, self.phonenum_field).send_keys("+79999999999")

    @allure.step('Переходим ко следующей форме оформления заказа.')
    def click_next_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.next_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.next_button).click()

    @allure.step('Выбираем дату доставки.')
    def set_date(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.date)))
        self.driver.find_element(By.CSS_SELECTOR, self.date).click()
        self.driver.find_element(By.CSS_SELECTOR, self.date).send_keys("03.09.2023")
        self.driver.find_element(By.CSS_SELECTOR, self.date).send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды.')
    def set_term(self, term_text):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.term_field)))
        self.driver.find_element(By.CSS_SELECTOR, self.term_field).click()
        list_terms = self.driver.find_elements(By.CSS_SELECTOR, self.term)
        for item in list_terms:
            if item.text == term_text:
                item.click()
                break

    @allure.step('Выбираем цвет.')
    def set_colour(self, colour):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "[id= '" + colour + "']")))
        self.driver.find_element(By.CSS_SELECTOR, "[id= '" + colour + "']").click()


    @allure.step('Заполняем поле "Комментарий".')
    def set_comment(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.comment)))
        self.driver.find_element(By.CSS_SELECTOR, self.comment).click()
        self.driver.find_element(By.CSS_SELECTOR, self.comment).send_keys("Комментарий")
        self.driver.find_element(By.CSS_SELECTOR, self.comment).send_keys(Keys.ENTER)

    @allure.step('Нажимаем на кнопку "Заказать".')
    def make_order_fin_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.make_an_order_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.make_an_order_button).click()
    @allure.step('Подтверждаем оформление заказа.')
    def order_confirmation_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.order_confirmation_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.order_confirmation_button).click()

    @allure.step('Проверяем, что заказ оформлен.')
    def check_order_was_made(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.order_made)))
        return self.driver.find_element(By.CSS_SELECTOR, self.order_made).text

    def check_status_button_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.check_status_button)))
        self.driver.find_element(By.CSS_SELECTOR, self.check_status_button).click()

    @allure.step('Переходим на главную страницу, кликнув по лого "Самокат".')
    def samokat_logo_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.samokat_logo)))
        self.driver.find_element(By.CSS_SELECTOR, self.samokat_logo).click()

    @allure.step('Проверяем, что перешли на главную страницу "Самокат".')
    def check_samokat_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.samokat_main_page)))
        return self.driver.find_element(By.CSS_SELECTOR, self.samokat_main_page).text

    @allure.step('Переходим на главную страницу Дзена, кликнув по лого "Яндекс".')
    def yandex_logo_click(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.yandex_logo)))
        self.driver.find_element(By.CSS_SELECTOR, self.yandex_logo).click()

    @allure.step('Проверяем, что перешли на главную страницу "Дзен".')
    def check_yandex_main_page(self):

        p = self.driver.current_window_handle
        chwd = self.driver.window_handles

        WebDriverWait(self.driver, 10).until(lambda driver: len(self.driver.window_handles) > 1)

        for w in chwd:
            if (w != p):
                self.driver.switch_to.window(w)
                break

        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.current_url == "https://dzen.ru/?yredirect=true")

        return self.driver.find_element(By.CSS_SELECTOR, self.dzen_main_page).is_displayed()

    def make_order(self, button_place, colour):

        if button_place == 'top':
            self.go_to_order_page_up()

        if button_place == 'bottom':
            self.scroll_page_down()
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