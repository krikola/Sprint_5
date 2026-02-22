from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
import data as data


class Test_Login:

    #Вход через кнопку "Войти в аккаунт" на главной странице
    def test_logout_login_in_main(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Войти в аккаунт" на главной странице 
        wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_IN_MAIN)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(data.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(data.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем подтверждение входа появлением кнопки "Оформить заказ" на главной странице
        assert wait.until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON)).is_displayed()
        
    #Вход через кнопку "Личный кабинет" на главной странице
    def test_logout_login_in_lk(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.main_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Личный кабинет" на главной странице
        wait.until(EC.element_to_be_clickable(TestLocators.LK_BUTTON)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(data.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(data.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем подтверждение входа появлением кнопки "Оформить заказ" на главной странице
        assert wait.until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON)).is_displayed()

    #Вход через кнопку в форме регистрации
    def test_logout_login_in_reg(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.register_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Войти" на странице регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_IN_REG)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(data.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(data.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем подтверждение входа появлением кнопки "Оформить заказ" на главной странице
        assert wait.until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON)).is_displayed()

    #Вход через кнопку в форме восстановления пароля
    def test_logout_login_in_forw_password(self, driver_chrome):
        driver = driver_chrome
        driver.get(data.forgot_url)
        wait = WebDriverWait(driver, 10)

        #Ожидаем отклика и кликаем на кнопку "Войти" на странице регистрации
        wait.until(EC.element_to_be_clickable(TestLocators.BUTTON_LOGIN_IN_PASS)).click()

        #Ожидаем перехода на страницу входа
        wait.until(EC.url_to_be(data.login_url))

        #Входим в аккаунт
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(data.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(data.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        #Ожидаем подтверждение входа появлением кнопки "Оформить заказ" на главной странице
        assert wait.until(EC.presence_of_element_located(TestLocators.ORDER_BUTTON)).is_displayed()

