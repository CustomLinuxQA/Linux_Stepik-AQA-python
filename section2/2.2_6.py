from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Создаем функцию calc(x)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    # Находим элемент Х
    x_element = browser.find_element(By.CSS_SELECTOR, ".form-group [id=input_value]")
    x = x_element.text
    y = calc(x)

    answer_string = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer_string)

    # вводим значение "y" в строку.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    check_box = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_box)

    # выбираем чекбокс - im the Robot
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)

    # выбираем радиобатон - Robots rule
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
