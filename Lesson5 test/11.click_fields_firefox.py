from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#сайт
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
#1000
input_field = driver.find_element(By.XPATH, "//input[@type='number']").send_keys("1000")
sleep(2)
#Очистка поля
input_field = driver.find_element(By.XPATH, "//input[@type='number']").clear()
sleep(2)
#999
input_field = driver.find_element(By.XPATH, "//input[@type='number']").send_keys("999")
sleep(2)
