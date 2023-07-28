import pytest
from pages.main_page import MainPage
from data.data import Expected_data
import allure

class TestMainPageQuestions:
    @allure.title('Проверка ответов на вопросы на главной странице.')
    @pytest.mark.parametrize('param, exp_answer',
                             [(1, Expected_data.expected_answer_1), (2, Expected_data.expected_answer_2),
                              (3, Expected_data.expected_answer_3), (4, Expected_data.expected_answer_4),
                              (5, Expected_data.expected_answer_5), (6, Expected_data.expected_answer_6),
                              (7, Expected_data.expected_answer_7), (8, Expected_data.expected_answer_8)])
    def test_questions(self, driver_fixt, param, exp_answer):
        main_page = MainPage(driver_fixt)
        main_page.scroll_page_down_to_questions()
        main_page.click_on_question(param)
        assert exp_answer == main_page.get_q_text(param), "Ожидаемый ответ - неправильный."