from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")

try:
    driver.find_element(By.NAME, "first_name").send_keys("John")
    driver.find_element(By.NAME, "last_name").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("john@example.com")
    driver.find_element(By.NAME, "phone").send_keys("9876543210")
    driver.find_element(By.NAME, "city").send_keys("Hyderabad")
    driver.find_element(By.NAME, "zip").send_keys("500001")
    driver.find_element(By.NAME, "website").send_keys("www.testing.com")

    driver.find_element(By.NAME, "comment").send_keys("This is an automated form submission test.")
    time.sleep(1)

    print("Form Autofill Test Successful!")

except Exception as e:
    print("Form Autofill Failed:", e)

finally:
    time.sleep(2)
    driver.quit()
