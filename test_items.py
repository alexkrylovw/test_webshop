from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  

def test_webshop(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")

    pagination_block = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "[type='submit']")))
    assert pagination_block == True, 'Button is not located!'