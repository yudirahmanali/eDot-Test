from selenium.webdriver.common.by import By

class CompanyPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.XPATH, "//button[contains(text(),'Add Company')]")
        self.name_input = (By.NAME, "company_name")
        self.save_button = (By.XPATH, "//button[contains(text(),'Save')]")

    def create_company(self, company_name):
        self.driver.find_element(*self.add_button).click()
        self.driver.find_element(*self.name_input).send_keys(company_name)
        self.driver.find_element(*self.save_button).click()
