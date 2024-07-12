from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
#Close
close_button = driver.find_element(By.XPATH, "//div[@id='modal']//p[text()='Close']").click()


