from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
from data import Urls
from data import Test_User

class Test_Logout:
    
    def test_logout_test_user(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.login_url)
        wait = WebDriverWait(driver, 10)

        # Входим в личный кабинет
        wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).send_keys(Test_User.test_user_email)
        wait.until(EC.presence_of_element_located(TestLocators.PASSWORD_INPUT)).send_keys(Test_User.test_user_password)
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()
       
        #Ожидаем перехода на главную страницу
        wait.until(EC.url_to_be(Urls.main_url))

        #Переходим в личный кабинет по кнопке
        wait.until(EC.element_to_be_clickable(TestLocators.LK_BUTTON)).click()
        wait.until(EC.url_to_be(Urls.profile_url))

        # Нажимаем кнопку "Выйти"
        wait.until(EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)).click()
    
        # Ожидаем перехода на страницу входа в аккаунт
        wait.until(EC.url_to_be(Urls.login_url))

        # Ожидаем, что форма логина отображается
        assert wait.until(EC.presence_of_element_located(TestLocators.EMAIL_INPUT)).is_displayed()





