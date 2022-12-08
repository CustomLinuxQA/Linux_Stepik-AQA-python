from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(r_browser):
    r_browser.get(link)
    r_browser.find_element(By.CSS_SELECTOR, "#login_link")


def test_guest_should_see_login_link_fail(r_browser):
    r_browser.get(link)
    r_browser.find_element(By.CSS_SELECTOR, "#magic_link")
# pytest -s -v --browser_name=firefox --reruns 1 --tb=line lesson6_step8_reruns.py
