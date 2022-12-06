from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "https://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.CSS_SELECTOR, ".form-group [id=input_value]")
        x = x_element.text
        y = calc(x)

        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, ".btn").click()
    finally:
        time.sleep(5)
