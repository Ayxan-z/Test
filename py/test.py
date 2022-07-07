from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("C:\\Users\\shahs\\Documents\\chromedriver.exe", options=options)
driver.get("https://fpay.az/guest/payments/new-payment/category/4951/merchant/5089")
sleep(2)
id_input = driver.find_element(By.CLASS_NAME, "MuiInputBase-input")
id_input.send_keys('')

submit_button = driver.find_element(By.CLASS_NAME, 'dashboard__params__button')
submit_button.click()
sleep(2)
money_input = driver.find_element(By.CLASS_NAME, 'MuiInputBase-adornedEnd')
money_input.send_keys('10')

