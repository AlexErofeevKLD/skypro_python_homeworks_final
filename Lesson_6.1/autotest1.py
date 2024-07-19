from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Base import *
from time import sleep

def test1(chrome_browser):
    chrome_browser.get(URL_1)
    form_data = {
    "First-name": First_name,
    "Last-name": Last_name,
    "Address": Address,
    "E-mail": Email,
    "Phone": Phone,
    "Zip-code": Zip_code,
    "City": City,
    "Country": Country,
    "Job-position": Job_position,
    "Company": Company
    }
    for field_name, value in form_data.items():
        chrome_browser.find_element(By.NAME, field_name).send_keys(value)
    WebDriverWait(chrome_browser, 40, 0.5).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    sleep(3)
    field_classes = {
        "First-name": "success",
        "Last-name": "success",
        "Address": "success",
        "E-mail": "success",
        "Phone": "success",
        "Zip-code": "danger",
        "City": "success",
        "Country": "success",
        "Job-position": "success",
        "Company": "success" 
    }

    for field_id, class_name in field_classes.items():
        assert class_name in chrome_browser.find_element(By.ID, field_id).get_attribute("class")