from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(r_browser):
    r_browser.get(link)
    r_browser.find_element(By.CSS_SELECTOR, "#login_link")
# error start pytest -s -v lesson6_step7_gecko.py
# pytest -s -v --browser_name=firefox lesson6_step7_gecko.py
