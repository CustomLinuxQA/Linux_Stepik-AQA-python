from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://suninjuly.github.io/selects1.html"


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        num1 = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)").text
        num2 = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)").text

        sum = int(num1) + int(num2)

        # Найдем значение атрибута. Обязательно сравниваем в формате string.
        Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(sum))

        # жмем Submit
        browser.find_element(By.CSS_SELECTOR, ".btn").click()

    finally:
        time.sleep(5)
