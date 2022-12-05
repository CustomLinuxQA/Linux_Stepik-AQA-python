from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


def link_t(link):
    # try: - убираем трай/кетчи, чтоб получить именно нужный ответ для Stepik
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("mail@example.com")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)
    # finally: - убираем трай/кетчи, чтоб получить именно нужный ответ для Stepik
    return browser.find_element(By.TAG_NAME, "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(link_t("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__": unittest.main()

# ответ
# FAILED (errors=1)
