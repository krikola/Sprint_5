from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators import TestLocators
from data import Urls

class Test_Navigation_Tab:

    #Соусы
    def test_navigation_to_sauces(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.main_url)
        wait = WebDriverWait(driver, 10)
        
        sauces_inactive = wait.until(EC.element_to_be_clickable(TestLocators.SAUCES_BUTTON))
        sauces_inactive.click()
        sauces_active = wait.until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB))
        assert 'current' in sauces_active.get_attribute('class')
   
    #Булки
    def test_navigation_to_rolls(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.main_url)
        wait = WebDriverWait(driver, 10)
        #Переход на вкладку "Соусы", для снятия активности с вкладки "Булки"
        sauces_inactive = wait.until(EC.element_to_be_clickable(TestLocators.SAUCES_BUTTON))
        sauces_inactive.click()
        wait.until(EC.visibility_of_element_located(TestLocators.SAUCES_TAB))

        rolls_inactive = wait.until(EC.element_to_be_clickable(TestLocators.ROLLS_BUTTON))
        rolls_inactive.click()
        rolls_active = wait.until(EC.visibility_of_element_located(TestLocators.ROLLS_TAB))
        assert 'tab_tab_type_current__' in rolls_active.get_attribute('class')
        
     #Начинки
    def test_navigation_to_topping(self, driver_chrome):
        driver = driver_chrome
        driver.get(Urls.main_url)
        wait = WebDriverWait(driver, 10)

        topping_inactive = wait.until(EC.element_to_be_clickable(TestLocators.TOPPINGS_BUTTON))
        topping_inactive.click()
        topping_active = wait.until(EC.visibility_of_element_located(TestLocators.TOPPINGS_TAB))
        assert 'current' in topping_active.get_attribute('class')
        

