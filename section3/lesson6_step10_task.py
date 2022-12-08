from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_add_to_basket(r_browser):
    r_browser.get(link)
    r_browser.implicitly_wait(5) # ставлю на всякий случай, если нагрузка на сервер или плохой интернет.
    r_browser.find_element(By.CSS_SELECTOR, ".dropdown-toggle").click()
    r_browser.implicitly_wait(5)  # ставлю на всякий случай, если нагрузка на сервер или плохой интернет.
    r_browser.find_element(By.CSS_SELECTOR, ".dropdown-submenu").click()
    r_browser.implicitly_wait(5)  # ставлю на всякий случай, если нагрузка на сервер или плохой интернет.
    r_browser.find_element(By.CSS_SELECTOR, "[title = 'Coders at Work']").click()
    buttons = r_browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) > 0, 'buttons not found'
