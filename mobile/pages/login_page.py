from appium.webdriver.common.appiumby import AppiumBy

class MobileLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.company_id = (AppiumBy.ID, "com.edot.ework:id/company_id")
        self.email_input = (AppiumBy.ID, "com.edot.ework:id/email")
        self.password_input = (AppiumBy.ID, "com.edot.ework:id/password")
        self.login_button = (AppiumBy.ID, "com.edot.ework:id/btn_login")

    def login(self, company_id, email, password):
        self.driver.find_element(*self.company_id).send_keys(company_id)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
