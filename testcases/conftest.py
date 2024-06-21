import os
import time
import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
        # for window import chrome webdriver
        # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        print("Launch chrome")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        # For window import gecko webdriver
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Launch firefox")
    elif browser == "edge":
        # For window import edge chromium webdriver
        # driver = webdriver.Edge(executable_path=(EdgeChromiumDriverManager().install())
        print(" Launch Edge")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(10)
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


import os


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        # Always add a URL to the report
        extras.append(pytest_html.extras.url("http://www.john.com/"))

        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Add screenshot on failure or skipped with xfail
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "-") + ".png"
            destination_file = os.path.join(report_directory, file_name)

            try:
                # Save screenshot
                driver.save_screenshot(destination_file)
                if file_name:
                    # Generate HTML for the screenshot
                    img_html = ("<div><img src='{}' alt='screenshot' style='width:300px;height:200px;'"
                                " onclick='window.open(this.src)' align='right'></div>".format(file_name))
                    extras.append(pytest_html.extras.html(img_html))
            except Exception as e:
                # Handle any exceptions during screenshot saving
                print(f"Failed to capture screenshot: {e}")

    report.extras = extras


def pytest_html_report_title(report):
    report.title = "DEMO Test report"
