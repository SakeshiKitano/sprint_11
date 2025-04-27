import time

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from data import Credentials
from locators import Locators
from curl import *


class TestPageTransitions:
    def login(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER))

    def test_personal_acc_click(self,driver):
        self.login(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACC))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        text = WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.PROFILE_LINK)).text
        assert text == 'Профиль'

    def test_from_personal_acc_to_construkor(self,driver):
        self.login(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACC))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.CONSTRUKT_BUTTON).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER)).text
        assert title == 'Оформить заказ'

    def test_exit_acc(self,driver):
        self.login(driver)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.PERSONAL_ACC))
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.PROFILE_LINK))
        driver.find_element(*Locators.EXIT_ACC_BUTTON).click()
        #time.sleep(4)
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER)).text
        assert reg_text == 'Вход'
        assert driver.current_url == main_site + 'login'
