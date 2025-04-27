import time

from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from data import Credentials
from locators import Locators
from curl import *

class TestConstruktor:

    def test_go_to_buns(self,driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        driver.find_element(*Locators.BUNS_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Булки')]]"))
        )
        assert active_tab.is_displayed(), "Таб 'Булки' не стал активным"

    def test_go_to_sauce(self,driver):
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Соусы')]]"))
        )
        assert active_tab.is_displayed(), "Таб 'Соусы' не стал активным"

    def test_go_to_fillings(self,driver):
        driver.find_element(*Locators.FILLINGS_BUTTON).click()
        active_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Начинки')]]"))
        )
        assert active_tab.is_displayed(), "Таб 'Начинки' не стал активным"


