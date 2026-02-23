import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
from data import Urls
from data_generators import generate_name, generate_login, generate_valid_password, generate_invalid_password

class Test_User_Registration:

    # Регистрация с валидными данными
    def test_successful_registration(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.register_url)
        wait = WebDriverWait(driver, 10)

        # Вводим сгенерированное имя, email и корректный пароль и нажимаем кнопку "Зарегистрироваться"
        wait.until(EC.presence_of_element_located(TestLocators.NAME_INPUT)).send_keys(generate_name())
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(generate_login())
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(generate_valid_password())
        wait.until(EC.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON)).click()
        
        # Ожидаем, что появится кнопка "Войти" на странице входа
        assert wait.until(EC.presence_of_element_located(TestLocators.LOGIN_BUTTON)).is_displayed()

    # Ошибка при регистрации с некорректным паролем
    def test_registration_with_invalid_password(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.register_url)
        wait = WebDriverWait(driver, 10)

        # Вводим сгенерированное имя, email и некорректный пароль и нажимаем кнопку "Зарегистрироваться"
        wait.until(EC.presence_of_element_located(TestLocators.NAME_INPUT)).send_keys(generate_name())
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(generate_login())
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(generate_invalid_password())
        wait.until(EC.element_to_be_clickable(TestLocators.REGISTRATION_BUTTON)).click()

        # Ожидаем появления сообщения об ошибке пароля
        assert wait.until(EC.presence_of_element_located(TestLocators.INCORRECTED_PASS)).is_displayed()
