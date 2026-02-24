from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
from data import Urls 
from data import Test_User


class Test_User_Navigation_To_Construction_And_Logo:
    
    #Перехож в конструктор по кнопке "Конструктор"
    def test_navigation_construction(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.main_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Войти в аккаунт" на главной странице 
        wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_IN_MAIN)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(Urls.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(Test_User.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(Test_User.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем переход на главную страницу
        wait.until(EC.url_to_be(Urls.main_url))
        
        #Переходим по кнопке "Личный кабинет"
        wait.until(EC.element_to_be_clickable(TestLocators.LK_BUTTON)).click()

        #Ожидаем переход в личный кабинет
        wait.until(EC.url_to_be(Urls.profile_url))

        #Кликаем на кнопку "Конструктор"
        wait.until(EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_BUTTON)).click()

        #Ожидаем перехода на станицу конструктора
        wait.until(EC.url_to_be(Urls.main_url))
        assert wait.until(EC.presence_of_element_located(TestLocators.CONSTRUCTOR_HEADER)).is_displayed()

    #Переход в конструктор по Лого сайта
    def test_navigation_logo(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.main_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Войти в аккаунт" на главной странице 
        wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_IN_MAIN)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(Urls.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(Test_User.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(Test_User.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем переход на главную страницу
        wait.until(EC.url_to_be(Urls.main_url))
        
        #Переходим по кнопке "Личный кабинет"
        wait.until(EC.element_to_be_clickable(TestLocators.LK_BUTTON)).click()

        #Ожидаем переход в личный кабинет
        wait.until(EC.url_to_be(Urls.profile_url))

        #Кликаем на лого "StellarBurgers"
        wait.until(EC.element_to_be_clickable(TestLocators.LOGO_BUTTON)).click()

        #Ожидаем перехода на главную страницу
        wait.until(EC.url_to_be(Urls.main_url))
        assert wait.until(EC.presence_of_element_located(TestLocators.CONSTRUCTOR_HEADER)).is_displayed()