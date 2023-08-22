import allure
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType


driver: webdriver.Remote


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def setup_teardown(request):
    # Setup
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")

    # run test
    yield

    # Teardown
    driver.quit()
