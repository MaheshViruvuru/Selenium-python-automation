import pytest
from selenium import webdriver
import time

from base_page import BasePage
from rahul_shetty_academy_page import PracticePage
#driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')


@pytest.mark.usefixtures('navigate_to_url')
class TestAmazonHomePage(BasePage):

    def test_navigate_to_rahul_shetty_academy_page(self):
        practice_page = PracticePage(self.driver)
        # menu = amazon_home_page.driver.find_element_by_id('nav-hamburger-menu')
        # menu.click()
        # customer_name = amazon_home_page.driver.find_element_by_id('hmenu-customer-name').text
        # text = self.driver.find_element_by_xpath('//h1[.="Practice Page"]')
        # print(text.text)
        print(practice_page.check_practice_page())

