from appium.webdriver.common.appiumby import AppiumBy

class CustomerPage:
    def __init__(self, driver):
        self.add_customer_button = (AppiumBy.ID, "com.edot.ework:id/btn_add_customer")
        self.name_input = (AppiumBy.ID, "com.edot.ework:id/customer_name")
        self.save_button = (AppiumBy.ID, "com.edot.ework:id/btn_save")

    def create_customer(self, name):
        self.driver.find_element(*self.add_customer_button).click()
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.save_button).click()
