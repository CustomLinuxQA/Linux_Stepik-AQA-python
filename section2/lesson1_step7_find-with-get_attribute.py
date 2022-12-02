from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Создаем функцию calc(x)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Находим элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, "[valuex]")

    # Возьмем значение атрибута "valuex"
    x_valuex = x_element.get_attribute("valuex")
    x = x_valuex
    y = calc(x)

    # вводим значение "y" в строку.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # выбираем чекбокс - im the Robot
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # выбираем радиобатон - Robots rule
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # жмем Submit
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option3.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
