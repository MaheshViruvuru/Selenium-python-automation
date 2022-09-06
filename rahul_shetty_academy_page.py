import time

from selenium.webdriver.common.by import By

from base_page import BasePage


class PracticePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    # amazon_logo = BasePage.Find(By.XPATH, '//a[@id="nav-logo-sprites"]')
    menu_button = (By.XPATH, '//a[@id="nav-hamburger-menu"]')
    get_customer_name = (By.XPATH, '//*[@id="hmenu-customer-name"]')
    practice_page_text = (By.XPATH, '//h1[.="Practice Page"]')
    drop_down_xpath = (By.XPATH, '//select[@id="dropdown-class-example"]')
    drop_down_xpath_value = (By.XPATH, '(//select[@id="dropdown-class-example"]//option)[1]')
    options_list = (By.XPATH, '//select[@id="dropdown-class-example"]//option')
    option1_xpath = (By.XPATH, '//select[@id="dropdown-class-example"]//option[.="Option1"]')

    def check_practice_page(self) -> bool:
        time.sleep(5)
        Practice_page_text = self.driver.find_element(*PracticePage.practice_page_text).text
        drop_down = self.driver.find_element(*PracticePage.drop_down_xpath)
        drop_down.click()
        options = self.driver.find_elements(*PracticePage.options_list)
        arr = []
        for option in options:
            arr.append(option)
        # arr.remove("")
        option1 = self.driver.find_element(*PracticePage.option1_xpath)
        print(option1.text)
        option1.click()
        drop_down_value = self.driver.find_element(*PracticePage.drop_down_xpath_value).text
        print(drop_down_value)
        return Practice_page_text
