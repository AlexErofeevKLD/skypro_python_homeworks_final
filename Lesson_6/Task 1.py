from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
options = webdriver.ChromeOptions()
options.add_argument('--disable-quic')
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.5)

try:
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
    text_from_content = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".bg-success"))).text
    print(text_from_content)

except Exception as ex:
    print(ex)
finally:
    driver.quit()
    