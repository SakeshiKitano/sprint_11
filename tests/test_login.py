

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Credentials
from locators import Locators



class TestLoginWithExistingCredentials:

    def test_login_from_main_page_button(self,driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER)).text
        assert title == 'Оформить заказ'

    def test_login_from_personal_account_button(self, driver):
        driver.find_element(*Locators.PERSONAL_ACC).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER)).text
        assert title == 'Оформить заказ'

    def test_login_from_registration_form(self,driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_LINK))
        driver.find_element(*Locators.REGISTER_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER)).text
        assert title == 'Оформить заказ'

    def test_login_from_restore_pass_form(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.REGISTER_LINK))
        driver.find_element(*Locators.RESTORE_PASS_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(Credentials.email)
        driver.find_element(*Locators.PASS_INPUT).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN_BUTTON_AUTH_PAGE).click()
        title = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER)).text
        assert title == 'Оформить заказ'
