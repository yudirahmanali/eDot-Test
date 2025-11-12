from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_marker = (By.XPATH, "//h1[contains(text(),'Dashboard')]")

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.dashboard_marker)) > 0
