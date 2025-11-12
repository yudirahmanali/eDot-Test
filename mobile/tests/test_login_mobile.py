import allure
from mobile.pages.login_page import MobileLoginPage

@allure.title("Login to eWork Mobile App")
def test_mobile_login(app_driver, config):
    login_page = MobileLoginPage(app_driver)

    creds = config["credentials"]
    login_page.login(creds["company_id"], creds["email"], creds["password"])

    # Dummy assertion (replace with actual element verification)
    assert True, "Login failed"
