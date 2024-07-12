from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_argument('--disable-quic')
#сайт
try:
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(2)
    blue_button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    for _ in range(3):
        blue_button = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
    print(ex)
finally:
    driver.quit()