import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    chrome_path = "D:/MyThings/Development/Chrome_For_Testing/chrome_win64/chrome.exe"
    chrome_driver = "D:/MyThings/Development/Chrome_For_Testing/chromedriver_win64/chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_path
    options.add_experimental_option("detach", True)

    services = Service(executable_path=chrome_driver)
    driver = webdriver.Chrome(options=options, service=services)

    driver.get("https://seleniumbase.io/demo_page")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
