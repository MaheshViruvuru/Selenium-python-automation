from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path='C:\Drivers\chromedriver_win32\chromedriver.exe')

driver.maximize_window()
driver.get('https://web.whatsapp.com/')
time.sleep(20)
action = ActionChains(driver)
contact = driver.find_elements_by_xpath('//*[@class="_3OvU8"]//span[.="Pepper"]').click()
# action.move_to_element(contact).click()

text_box = driver.find_elements_by_xpath('(//*[@role="textbox"])[2]').send_keys('This is an automated message')

send_button = driver.find_elements_by_xpath('//*[@data-icon="send"]').click()
