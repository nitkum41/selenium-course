from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")

###alerts
# driver.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()
# driver.switch_to.alert.accept()
# time.sleep(2)

# driver.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
# driver.switch_to.alert.dismiss()
# time.sleep(2)

# driver.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
# driver.switch_to.alert.send_keys("hello world")
# time.sleep(2)

# driver.switch_to.alert.accept()

##windows

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)

searchlinks=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']//div[@id='wikipedia-search-result-link']//a")

for link in searchlinks:
    link.click()
    time.sleep(1)
    # winid=driver.current_window_handle
    # driver.switch_to.window(winid)
    # print(driver.title)


windowids = driver.window_handles
for winid in windowids:
    driver.switch_to.window(winid)
    print(driver.title)

time.sleep(2)
driver.close()





