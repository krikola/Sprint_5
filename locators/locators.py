from selenium.webdriver.common.by import By


class TestLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")                #Поле Email
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")                   #Поле Имя
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")            #Поле Пароль
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button__33qZ0")                             #Кнопка Войти
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")                   #Кнопка Зарегестрироваться
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")                                      #Кнопка выход
    LK_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")                                    #Кнопка Личный Кабинет
    BUTTON_LOGIN_IN_MAIN = (By.XPATH, './/button[text() = "Войти в аккаунт"]')                  #Кнопка войти на главнйо странице
    REGISTRATION_BUTTON_LOGIN = (By.XPATH, '//a[text() = "Зарегистрироваться"]')                #Ссылка на кнопку зарегестрироваться
    INCORRECTED_PASS = (By.XPATH, '//p[text() = "Некорректный пароль"]')                        #Ошибка некорректный пароль
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Оформить заказ']")             #Кнопка оформить заказ
    BUTTON_LOGIN_IN_REG = (By.XPATH, "//a[normalize-space(text())='Войти']")                    #Кнопка войти на странице регистрации
    BUTTON_LOGIN_IN_PASS = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")                              #Кнопка войти на странице восстановления пароля
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[.//p[normalize-space(text())='Конструктор']]")         #Кнопка конструктор в личном кабинете
    LOGO_BUTTON = (By.CSS_SELECTOR, 'a[href="/"]')                                              #Навигация для лого в личном кабинете
    CONSTRUCTOR_HEADER = (By.XPATH, ".//*[text()='Соберите бургер']")                           #Навигация для Заголовка "Соберите бургер"
    ROLLS_BUTTON = (By.XPATH, '//span[text()="Соусы"]/..')                                      #Для таба «Булки»
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Начинки"]/..')                                   #Для таба «Соусы»
    TOPPINGS_BUTTON = (By.XPATH, '//span[text()="Булки"]/..')                                   #Для таба «Начинки»

 
