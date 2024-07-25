from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Base import URL_2


def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)

    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)

    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    wait = WebDriverWait(chrome_browser, 46)
    wait.until(EC.invisibility_of_element_located((By.ID, "spinner")))

    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text
    assert result_text == "15"
    print(result_text)
