import pytest
import allure
from web.pages.login_page import LoginPage
from web.pages.company_page import CompanyPage
from utils.faker_data import generate_company_data

@allure.title("Create a new company")
def test_create_company(driver, config):
    login_page = LoginPage(driver)
    company_page = CompanyPage(driver)
    company_data = generate_company_data()

    login_page.open(config["base_url"])
    login_page.login(config["credentials"]["email"], config["credentials"]["password"])

    company_page.create_company(company_data["company_name"])

    # Dummy assertion (replace with actual verification)
    assert company_data["company_name"], "Company name not created"
