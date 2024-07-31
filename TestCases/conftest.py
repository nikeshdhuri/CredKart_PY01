import pytest
from selenium import webdriver
from Utilities.Readproperties import ReadconfigClass

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture
def setup(request):
    loginurl = ReadconfigClass.get_login_url()

    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        print("Test Run - Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(loginurl)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Nikesh"
    metadata.pop("Plugins", None)



@pytest.fixture(params=[
    ("nik3@gmail.com", "Nik@123", "pass"),
    ("2nik3@gmail.com", "Nik@123", "fail"),
    ("nik3@gmail.com", "Nik@1231", "fail"),
    ("nik3@gmail.com1", "Nik@1231", "fail")
])
def getDataForLogin(request):
    return request.param



