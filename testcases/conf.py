import pytest


@pytest.fixture(autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("Provide valid browser")
    print("Login")
    print("Browse products")
    yield
    print("logoff")
    print("Close browser")


def pytest_adoption(parser):
    parser.adoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")



