import pytest
from selenium import webdriver

@pytest.fixture
def driver_fixt():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()