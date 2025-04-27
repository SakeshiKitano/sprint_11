import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")  # Задаем размер окна
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
    driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
    driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()

    return driver
