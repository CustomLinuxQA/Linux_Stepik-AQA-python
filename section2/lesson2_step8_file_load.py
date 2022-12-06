from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://suninjuly.github.io/file_input.html"


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.NAME, "firstname").send_keys("Ivan")
        browser.find_element(By.NAME, "lastname").send_keys("Petrov")
        browser.find_element(By.NAME, "email").send_keys("email")

        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
        browser.find_element(By.NAME, "file").send_keys(file_path)

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        time.sleep(5)
