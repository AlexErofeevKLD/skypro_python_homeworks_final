from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(2)
#Кнопка 5 раз
for _ in range(5):
    add_button = driver.find_element(By.XPATH, "//*[@id='content']/div[1]/button[1]").click()
sleep(1)
#список
delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
#размер списка
print(f"Размер списка: {len(delete_buttons)}")