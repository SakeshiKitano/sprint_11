import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from data import Credentials
from locators import Locators


@pytest.fixture
def driver(scope="function"):
    options = Options()
    options.add_argument("--window-size=1920,1080")  # Задаем размер окна
    driver = webdriver.Chrome(options=options)
    driver.get(main_site)
    yield driver
    driver.quit()
