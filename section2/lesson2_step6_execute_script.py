from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = browser.find_element(By.CSS_SELECTOR, ".form-group [id=input_value]").text
        y = calc(x)

        answer_string = browser.find_element(By.ID, "answer")
        browser.execute_script("return arguments[0].scrollIntoView(true);", answer_string)
        browser.find_element(By.ID, "answer").send_keys(y)

        check_box = browser.find_element(By.ID, "robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)
        browser.find_element(By.ID, "robotCheckbox").click()

        radio_button = browser.find_element(By.ID, "robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
        browser.find_element(By.ID, "robotsRule").click()

        button = browser.find_element(By.CSS_SELECTOR, "button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        time.sleep(5)
