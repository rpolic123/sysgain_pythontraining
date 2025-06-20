from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/form")

driver.find_element(By.NAME, 'name').send_keys('John Doe')
driver.find_element(By.NAME, 'email').send_keys('john@example.com')
driver.find_element(By.ID, 'submit').click()
print("Form submitted.")
driver.quit()