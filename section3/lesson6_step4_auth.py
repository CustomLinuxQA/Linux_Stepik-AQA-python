from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from os import getenv

load_dotenv()
link = "https://stepik.org/lesson/236895/step/1"
AUTH_EMAIL = getenv('AUTH__EMAIL')
AUTH_PASSWORD = getenv('AUTH__PASSWORD')


class TestStepikPage():

    def test_login(self, driver):
        driver.get(link)
        driver.implicitly_wait(15)  # Stepik иногда очень долго открывается.
        driver.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()

    def test_fill_login_form(self, driver):
        driver.find_element(By.ID, "id_login_email").send_keys(AUTH_EMAIL)
        driver.find_element(By.ID, "id_login_password").send_keys(AUTH_PASSWORD)
        driver.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
