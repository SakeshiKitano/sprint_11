from selenium.webdriver.common.by import By


class Locators:
    # кнопка "войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # поле ввода Имя формы регистрации
    NAME_INPUT = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")
    # поле ввода Email формы регистрации
    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    # полe ввода Пароль формы регистрации
    PASS_INPUT = (By.XPATH, "//fieldset[@class='Auth_fieldset__1QzWN mb-6']//input[@type='password']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # кнопка Войти на форме входа в акк
    LOGIN_BUTTON_AUTH_PAGE = (By.XPATH, "//button[text()='Войти']")
    #ссылка на логин, на форме регистрации
    LOGIN_LINK=(By.XPATH, "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']/a[text()='Войти']")
    # ссылка на регистрацию, на форме входа в аккаунт
    REGISTER_LINK = (By.XPATH,
                     "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']/a[text='Зарегистрироваться']")
