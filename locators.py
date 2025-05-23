from selenium.webdriver.common.by import By

class Locators:
    # кнопка "войти в аккаунт" на главной странице
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//section[@class='BurgerConstructor_basket__29Cd7 mt-25 ']//button[text()='Войти в аккаунт']")
    #LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[@class = button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg]")
    # поле ввода Имя формы регистрации
    NAME_INPUT = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input")
    # поле ввода Email формы регистрации
    EMAIL_INPUT = (By.XPATH, "//div[label[contains(text(),'Email')]]//input")
    # полe ввода Пароль формы регистрации
    PASS_INPUT = (By.XPATH, "//div[@class='input__container']//input[@name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20']/button[text()='Зарегистрироваться']")
    # кнопка Войти на форме входа в акк
    LOGIN_BUTTON_AUTH_PAGE = (By.XPATH, "//button[text()='Войти']")
    #ссылка на логин, на форме регистрации
    LOGIN_LINK=(By.XPATH,
                "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']/a[text()='Войти']")
    # ссылка на регистрацию, на форме входа в аккаунт
    REGISTER_LINK = (By.XPATH,
                     "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']/a[text()='Зарегистрироваться']")
    # Хедер Вход
    LOGIN_HEADER = (By.XPATH, "//main[@class = 'App_componentContainer__2JC2W']//h2[text()='Вход']")
    #хеддер Регистрация
    REGISTER_HEADER = (By.CSS_SELECTOR, "h2:contains('Регистрация')")
    #Сообщение Некорректный пароль
    ERROR_MESSAGE = (By.XPATH, "//form[@class = 'Auth_form__3qKeq mb-20']//p[text()='Некорректный пароль']")
    #Ссылка Личный кабинет
    PERSONAL_ACC = (By.XPATH, "//nav[@class= 'AppHeader_header__nav__g5hnF']//p[text() = 'Личный Кабинет']")
    #кнопка Оформить заказ
    PLACE_ORDER = (By.XPATH,"//section[@class = 'BurgerConstructor_basket__29Cd7 mt-25 ']//button[text() = 'Оформить заказ']")
    #ссылка Восстановить пароль
    RESTORE_PASS_LINK = (By.XPATH, "//div[@class = 'Auth_login__3hAey']//a[text() = 'Восстановить пароль']")
    #ссылка Профиль
    PROFILE_LINK = (By.XPATH, "//div[@class = 'Account_account__vgk_w']//a[text()= 'Профиль']")
    #кнопка Конструктор
    CONSTRUKT_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and p[contains(text(), 'Конструктор')]]")
    #кнопка Выход из аккаунта
    EXIT_ACC_BUTTON = (By.XPATH, "//div[@class = 'Account_account__vgk_w']//button[text()= 'Выход']")
    # Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//span[contains(text(),'Булки')]")
    # Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, ".//span[contains(text(),'Соусы')]")
    # Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, ".//span[contains(text(),'Начинки')]")
    ACTIVE_BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Булки')]]")
    ACTIVE_SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Соусы')]]")
    ACTIVE_FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_type_current') and span[contains(text(), 'Начинки')]]")

