# https://opensource-demo.orangehrmlive.com/
# username: Admin
# password: admin123
# login
# password
# capture title
# verfiy titleof page: OrangeHRM


# object of chrome class and launch browser executable_path is optional
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# capabilities = DesiredCapabilities.CHROME.copy()

# capabilities['acceptInsecureCerts'] = True

#in pthon 3.12 onwards it treats \G as special character so add r"" to the beginning of string

# service = Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

# options=Options()
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# options.add_argument('--allow-insecure-localhost')
# options.add_argument('--ignore-urlfetcher-cert-requests')

# options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--start-maximized")

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()


driver.get("https://opensource-demo.orangehrmlive.com/")

driver.implicitly_wait(3)

# WebDriverWait(driver, timeout=5).until(title_is,"OrangeHRM")

driver.find_element(by=By.NAME,value="username").send_keys("Admin")
driver.find_element(by=By.NAME,value="password").send_keys("admin123")
driver.find_element(by=By.CSS_SELECTOR,value="button").click()


actual_title=driver.title

expected_title="OrangeHRM"

if actual_title == expected_title:
    print("Login test passed")
else:
    print("Login test failed")


driver.close()