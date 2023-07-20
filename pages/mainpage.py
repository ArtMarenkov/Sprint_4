from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
class MainPage:


    exp_t_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    exp_t_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    exp_t_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    exp_t_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    exp_t_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    exp_t_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    exp_t_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    exp_t_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    question = 'accordion__heading-'
    question_text = 'accordion__panel-'

    @allure.step('Открываем страницу в браузере')
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

    @allure.step('Прокручиваем страницу вниз.')
    def scroll_page_down(self):
        q_first = self.driver.find_element(By.ID, 'accordion__heading-0')
        self.driver.execute_script('arguments[0].scrollIntoView();', q_first)

    @allure.step('Выбираем вопрос № {param}')
    def click_on_question(self, param):
        real_param = str(param - 1)
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable((By.ID, self.question + real_param)))
        self.driver.find_element(By.ID, self.question + real_param).click()

    @allure.step('Получаем текст ответа на вопрос №{param}')
    def get_q_text(self, param):
        real_param = str(param - 1)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, self.question_text + real_param)))
        return self.driver.find_element(By.ID, self.question_text + real_param).text