from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#сайт
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)
#data
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
sleep(2)
#login
login_button = driver.find_element(By.XPATH, "//button['Login']").click()
sleep(2)