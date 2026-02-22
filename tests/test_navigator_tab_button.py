from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
import data
import time 

class Test_User_Navigation_To_Construction_And_Logo:

    def test_navigation_construction(self, driver_chrome):
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

        #Ожидаем переход на главную страницу
        wait.until(EC.url_to_be(data.main_url))

        #Кликаем на кнопку "Соусы"
        wait.until(EC.element_to_be_clickable(TestLocators.SAUCES_BUTTON)).click()
        time.sleep(1.5)

        #Кликаем на кнопку "Начинки"
        wait.until(EC.element_to_be_clickable(TestLocators.TOPPINGS_BUTTON)).click()
        time.sleep(1.5)

        #Кликаем на кнопку "Булки"
        wait.until(EC.element_to_be_clickable(TestLocators.ROLLS_BUTTON)).click()
        time.sleep(1.5)

        
        

