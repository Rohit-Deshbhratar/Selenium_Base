import os.path
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service


@pytest.fixture(autouse=True)
def setup(request, browser):
    global driver
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

    driver.get("https://seleniumbase.io/demo_page02")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", default="firefox")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.rcvacademy.com/"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = str(int(round(time.time() * 1000)))
            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_file = os.path.join(report_directory, file_name)
            driver.save_screenshot(destination_file)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html(html))
        report.extras = extras


def pytest_html_report_title(report):
    report.title = "Selenium Base Report"
