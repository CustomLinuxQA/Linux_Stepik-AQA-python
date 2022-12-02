from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time, math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Создаем функцию calc(x)
    def calc(x):
        return str(num1 + num2)


    # Находим элементы
    id_num1 = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(2)")
    id_num2 = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(4)")

    # Определяем значение строки
    num1 = id_num1.text
    num2 = id_num2.text

    # Посчитаем сумму
    sum = int(num1) + int(num2)

    # Найдем значение атрибута. Обязательно сравниваем в формате string.
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum))

    # жмем Submit
    option2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    option2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
