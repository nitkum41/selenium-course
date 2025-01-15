from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# service = Service(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# options = Options()
# options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
# options.add_argument("--remote-debugging-port=9222")
# # options.add_argument("--start-maximized")
# options.add_experimental_option("detach", True)

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

driver.maximize_window()

driver.implicitly_wait(10)

#absolut epath
# driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin")
# driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin123")
# driver.find_element(by=By.XPATH,value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()

#relative xpath

# driver.find_element(by=By.XPATH,value="//input[@placeholder='Username']").send_keys("Admin")
# driver.find_element(by=By.XPATH,value="//input[@placeholder='Password']").send_keys("admin123")
# driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()





# driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
#
# driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
#
# driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

## use of and or

# driver.find_element(by=By.XPATH,value="//input[@name='username' and @placeholder='Username']").send_keys("Admin")
# driver.find_element(by=By.XPATH,value="//input[@name='password' or @placeholder='Password']").send_keys("admin123")
# driver.find_element(by=By.XPATH,value="//button[@type='submit']").click()

## contains() //   starts-with()
driver.find_element(by=By.XPATH,value="//input[contains(@name,'user')]").send_keys("Admin")
driver.find_element(by=By.XPATH,value="//input[starts-with(@name,'pass')]").send_keys("admin123")

# driver.find_element(by=By.XPATH,value="//button[starts-with(@type,'su')]").click()

## text()
driver.find_element(by=By.XPATH,value="//button[text()=' Login ']").click()

driver.close()