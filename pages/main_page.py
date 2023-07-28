from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from data.locators import Locators
import allure

class MainPage(Base_page):
    @allure.step('Прокручиваем страницу вниз.')
    def scroll_page_down_to_questions(self):
        Base_page.scroll_to_element(self, By.ID, Locators.according_heading)

    @allure.step('Выбираем вопрос № {param}')
    def click_on_question(self, param):
        real_param = str(param - 1)
        Base_page.wait_for_element_is_clickable(self, By.ID, Locators.question + real_param)
        Base_page.click_on_element(self, By.ID, Locators.question + real_param)

    @allure.step('Получаем текст ответа на вопрос №{param}')
    def get_q_text(self, param):
        real_param = str(param - 1)
        Base_page.wait_for_element(self, By.ID, Locators.question_text + real_param)
        return Base_page.get_element_text(self, By.ID, Locators.question_text + real_param)