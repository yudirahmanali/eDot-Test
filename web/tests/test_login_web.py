import pytest
import allure
from web.pages.login_page import LoginPage
from web.pages.dashboard_page import DashboardPage

@allure.title("Login to eSuite Web")
def test_login_success(driver, config):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.open(config["base_url"])
    login_page.login(config["credentials"]["email"], config["credentials"]["password"])

    assert dashboard_page.is_logged_in(), "Login failed - Dashboard not visible"
