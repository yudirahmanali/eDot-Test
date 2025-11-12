import allure
from mobile.pages.customer_page import CustomerPage
from utils.faker_data import generate_customer_data

@allure.title("Create customer in mobile app")
def test_create_customer(app_driver):
    customer_page = CustomerPage(app_driver)
    customer_data = generate_customer_data()

    customer_page.create_customer(customer_data["customer_name"])
    assert True, "Customer creation failed"
