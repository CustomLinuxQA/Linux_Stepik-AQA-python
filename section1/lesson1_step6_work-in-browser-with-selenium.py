from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    button.click()


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()