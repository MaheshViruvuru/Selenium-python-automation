import pytest
from selenium import webdriver
driver = None


@pytest.fixture()
def navigate_to_url(request):
    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    request.cls.driver = driver
    # text = driver.find_element_by_xpath('//h1[.="Practice Page"]')
    # print(text.text)
    yield
    driver.close()
    driver.quit()

# import pytest
# from selenium import webdriver
# import time
# driver = None
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )
#
#
# @pytest.fixture(scope="class")
# def setup(request):
#     global driver
#     browser_name=request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#     elif browser_name == "IE":
#         print("IE driver")
#     driver.get("https://rahulshettyacademy.com/angularpractice/")
#     driver.maximize_window()
#
#     request.cls.driver = driver
#     yield
#     driver.close()
