import pytest
from selenium import webdriver
import yaml

@pytest.fixture(scope="session")
def config():
    with open("web/config/web_config.yaml") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
