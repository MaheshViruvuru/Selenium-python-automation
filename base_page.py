from selenium import webdriver


class BasePage:
    driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

    def Find(self, locator, value):
        element = self.driver.find_element(by=locator, value=value)
        return element