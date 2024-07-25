from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Base import URL_1, first_name, last_name, address, email, phone, \
zip_code, city, country, job_position, company
from time import sleep


def test_data_types_form(chrome_browser):
    chrome_browser.get(URL_1)
    form_data = {
    "first-name": first_name,
    "last-name": last_name,
    "address": address,
    "e-mail": email,
    "phone": phone,
    "zip-code": zip_code,
    "city": city,
    "country": country,
    "job-position": job_position,
    "company": company
    }
    for field_name, value in form_data.items():
        chrome_browser.find_element(By.NAME, field_name).send_keys(value)

    WebDriverWait(chrome_browser, 40, 0.5).until(EC.element_to_be_clickable
    ((By.TAG_NAME, "button"))).click()
    sleep(3)
    field_classes = {
        "first-name": "success",
        "last-name": "success",
        "address": "success",
        "e-mail": "success",
        "phone": "success",
        "zip-code": "danger",
        "city": "success",
        "country": "success",
        "job-position": "success",
        "company": "success"
    }

    for field_id, class_name in field_classes.items():
        elements = chrome_browser.find_elements(By.ID, field_id)

    assert any(class_name in element.get_attribute
        ("class") for element in elements)
