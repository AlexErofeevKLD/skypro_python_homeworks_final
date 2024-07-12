from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
try:
    count = 0
    driver.get("http://uitestingplayground.com/classattr")
    sleep(2)
    for _ in range(3):
        blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
        sleep(2)
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    driver.quit()


