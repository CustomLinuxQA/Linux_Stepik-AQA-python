import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

chromedriver_autoinstaller.install()
geckodriver_autoinstaller.install()





@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="class")
def driver():
    print("\nstart browser for test..")
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def r_browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    r_browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        r_browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        r_browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield r_browser
    print("\nquit browser..")
    r_browser.quit()
