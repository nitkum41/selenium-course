from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains,Keys ##import Keys class
import time

driver=webdriver.Chrome()

driver.get("https://text-compare.com/")

driver.implicitly_wait(3)
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)

### select keys Ctl+A on input1 box

# act.key_down(Keys.CONTROL)  ##press key
# act.send_keys("a")   ##alphabet
# act.key_up(Keys.CONTROL)  ##release key
# act.perform()  ##perform action

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

## copy test Ctrl+C on input1 box

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

## press tab key to navigate to input 2 box

act.send_keys(Keys.TAB).perform()


## press Ctrl+V in imput2 

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


time.sleep(4)

driver.quit()


