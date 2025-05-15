import time
from selenium.webdriver.common.by import By
import pytest

# Test case to verify login functionality with valid and invalid data
def test_login(setup, login_data):
    driver = setup
    valid_data, invalid_data = login_data

    # Loop through valid data and perform login
    for username, password in valid_data:
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        # Verify if login was successful
        time.sleep(10)  # Wait for the page to load
        if driver.title == "Swag Labs":
            assert True
        else:
            assert False

        # # Logout (if applicable)
        if driver.title == "Swag Labs":
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            time.sleep(2)
            driver.find_element(By.ID, "logout_sidebar_link").click()
            time.sleep(1)


    # Loop through invalid data and verify error message
    for username, password in invalid_data:
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        # Verify error message
        time.sleep(2)  # Wait for the error message to load
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Username and password do not match any user in this service"
