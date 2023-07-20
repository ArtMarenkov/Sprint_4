import pytest
from pages.mainpage import MainPage
from selenium import webdriver
import allure

class TestMainPageQuestions:
    
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка ответов на вопросы на главной странице.')
    @pytest.mark.parametrize('param, exp_text', [(1, MainPage.exp_t_1), (2, MainPage.exp_t_2), (3, MainPage.exp_t_3), (4, MainPage.exp_t_4), (5, MainPage.exp_t_5), (6, MainPage.exp_t_6), (7, MainPage.exp_t_7), (8, MainPage.exp_t_8)])
    def test_questions(self, param, exp_text):
        main_page = MainPage(self.driver)
        main_page.scroll_page_down()
        main_page.click_on_question(param)

        assert exp_text == main_page.get_q_text(param)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()