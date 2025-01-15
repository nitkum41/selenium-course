from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

driver.maximize_window()

# button = driver.find_element(By.XPATH,"//button[@id='register-button']")

# print(button.is_displayed())
# print(button.is_enabled())
gender_before = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(gender_before.is_selected())

gender_before.click() #select radio button

gender_after = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print(gender_after.is_selected())







driver.close()
