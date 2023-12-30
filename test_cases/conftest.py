import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        chrome_path = r"D:/MyThings/Development/Chrome_For_Testing/chrome-win64/chrome.exe"
        chrome_driver = r"D:/MyThings/Development/Chrome_For_Testing/chromedriver-win64/chromedriver.exe"

        options = webdriver.ChromeOptions()
        options.binary_location = chrome_path
        options.add_experimental_option("detach", True)

        services = Service(executable_path=chrome_driver)
        driver = webdriver.Chrome(options=options, service=services)
    elif browser == "firefox":
        firefox_driver = "D:/MyThings/Development/Chrome_For_Testing/geckodriver/geckodriver.exe"

        option = webdriver.FirefoxOptions()
        service = Service(executable_path=firefox_driver)

        driver = webdriver.Firefox(options=option, service=service)

    driver.get("https://seleniumbase.io/demo_page")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
