import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Test case to verify login functionality with valid and invalid data
def test_login(setup, login_data):
    driver = setup
    valid_data = login_data

    # Loop through valid data and perform login
    for username, password in valid_data:
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)  # Wait for the page to load
        try:
            assert driver.title == "Swag Labs"
            driver.find_element(By.ID, "react-burger-menu-btn").click()
            logoutBtn = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
            logoutBtn.click()
        except:
            error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
            assert error_message == "Epic sadface: Sorry, this user has been locked out."
