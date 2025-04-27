import time
from calendar import firstweekday
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from data import Credentials
from helper import generate_registration_data, generate_password, generate_registration_name_and_email
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_sucsess_registration(self, driver):
        #arrange
        first_name, email, password = generate_registration_data()

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_LINK))
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(first_name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        #time.sleep(2)
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER)).text
        assert reg_text == 'Вход'
        assert driver.current_url == main_site + 'login'

    @pytest.mark.parametrize('quantity', [1, 4, 5])
    def test_registration_failed_password(self, driver, quantity):
        first_name, email = generate_registration_name_and_email()
        password = generate_password(quantity)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_LINK))
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(first_name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ERROR_MESSAGE)).text
        assert message == 'Некорректный пароль'
        assert driver.current_url == main_site + 'register'