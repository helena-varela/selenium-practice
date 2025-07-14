from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret")
    driver.find_element(By.ID, "login-button").click()

    assert "inventory.html" in driver.current_url
    time.sleep(5)
    print("✅ Login Realizado com sucesso! ")

except AssertionError:
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    print(f"❌ Falha no login: {error_message}")

finally:
    driver.quit()