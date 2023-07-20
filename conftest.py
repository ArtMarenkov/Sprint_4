import pytest
from selenium import webdriver

@pytest.fixture
def driver_fixt():

    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")

    yield driver
    driver.quit()