from faker import Faker

fake = Faker()

def generate_company_data():
    return {
        "company_name": fake.company(),
        "address": fake.address(),
        "phone": fake.phone_number(),
        "email": fake.company_email()
    }

def generate_customer_data():
    return {
        "customer_name": fake.name(),
        "phone": fake.phone_number(),
        "email": fake.email(),
        "address": fake.address()
    }
