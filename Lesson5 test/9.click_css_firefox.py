from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#сайт
driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)
#Синяя кнопка
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary").click()


