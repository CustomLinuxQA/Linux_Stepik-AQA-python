import time, math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_fill_form():
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # говорим Selenium проверять в течение 12 секунд, пока значение "price" не станет равным "$100"
        # Это пауза построчного кода. button выполнится, как только будет выполнено условие price
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

        browser.find_element(By.ID, "book").click()
        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "solve").click()

    finally:
        time.sleep(5)
