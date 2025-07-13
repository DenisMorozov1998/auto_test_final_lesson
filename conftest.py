import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test..")
        print(f"Language: {language}")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test..")
        print(f"Language: {language}")
        options = webdriver.FirefoxOptions()
        options.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

