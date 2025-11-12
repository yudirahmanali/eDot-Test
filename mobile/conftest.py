import pytest
from appium import webdriver
import yaml

@pytest.fixture(scope="session")
def config():
    with open("mobile/config/mobile_config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def app_driver(config):
    desired_caps = {
        "deviceName": config["deviceName"],
        "platformName": config["platformName"],
        "appPackage": config["appPackage"],
        "appActivity": config["appActivity"],
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()
