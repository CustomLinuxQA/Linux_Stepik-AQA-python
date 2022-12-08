import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser_func():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser_func):
        print("start test1")
        browser_func.get(link)
        browser_func.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser_func):
        print("start test2")
        browser_func.get(link)
        browser_func.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")
