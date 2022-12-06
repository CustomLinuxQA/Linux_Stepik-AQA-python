from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, ".btn").click()

        alert = browser.switch_to.alert
        alert.accept()

        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(5)
