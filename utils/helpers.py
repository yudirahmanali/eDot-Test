def take_screenshot(driver, name="screenshot"):
    driver.save_screenshot(f"reports/{name}.png")
