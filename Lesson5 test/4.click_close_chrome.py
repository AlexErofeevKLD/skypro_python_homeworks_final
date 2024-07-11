from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
#сайт
driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
#Close
close_button = driver.find_element(By.XPATH, "//div[@id='modal']//p[text()='Close']").click()


