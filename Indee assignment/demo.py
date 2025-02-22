import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()




### step 1

url = "https://indeedemo-fyc.watch.indee.tv/"
pin = "WVMVHWBS"

driver.get(url)

driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='access-code']").send_keys(pin)

driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(5)

target_link = driver.find_element(By.XPATH,"//*[contains(text(), 'Test automation project')]")
driver.execute_script("arguments[0].scrollIntoView();",target_link)

target_link.click()


time.sleep(2)

detail_link = driver.find_element(By.XPATH,"//*[@id='detailsSection']")
driver.execute_script("arguments[0].scrollIntoView();",detail_link)

detail_link.click()

time.sleep(10)

driver.find_element(By.XPATH,"//*[@id='videosSection']").click()

time.sleep(2)

video_link = driver.find_element(By.XPATH,"//button[@aria-label='Play Video']")
driver.execute_script("arguments[0].scrollIntoView();",video_link)

video_link.click()

time.sleep(10)



####video is inside a frame so switch to iframe

driver.switch_to.frame("video_player")



### pause the video


my_wait = WebDriverWait(driver,10 , poll_frequency=2 , ignored_exceptions=[NoSuchElementException,Exception,
                                                                           ElementNotVisibleException,ElementNotSelectableException])

video_element = my_wait.until(EC.presence_of_element_located((By.TAG_NAME,"video")))

time.sleep(5)
if 'paused' in video_element.get_attribute('class'):
    video_element.click()  # Play the video
else:
    video_element.click()  # Pause the video


time.sleep(5)


## go back to main page

driver.switch_to.default_content()

### replay using continue watching
driver.find_element(By.XPATH,"//button[@aria-label='Continue Watching']").click()


# Wait for a while to see the result
time.sleep(10)


### set volume

####video is inside a frame so switch to iframe

driver.switch_to.frame("video_player")
# video_element = my_wait.until(EC.presence_of_element_located((By.TAG_NAME,"video")))

if video_element:
    # Set volume using JavaScript (volume value between 0.0 and 1.0, where 1 is full volume)
    volume = 0.5  # Set to 50% volume
    driver.execute_script(f"arguments[0].volume = {volume};", video_element)
    print("volume set to 50")
    # Play the video
    # video_element.click()



try:

    ##hover over the video
    actions = ActionChains(driver)
    actions.move_to_element(video_element).perform()

    settings_button = driver.find_element(By.XPATH,"//div[@aria-label='Settings']")

    actions.move_to_element(settings_button).click().perform()

    button_480p=driver.find_element(By.XPATH,"//button[@aria-label='480p']")

    actions.move_to_element(button_480p).click().perform()
    time.sleep(10)

    ##hover over the video
    actions.move_to_element(video_element).perform()

    actions.move_to_element(settings_button).click().perform()

    button_720p = driver.find_element(By.XPATH,"//button[@aria-label='720p']")
    actions.move_to_element(button_720p).click().perform()

    time.sleep(10)
except Exception as e:
    print("Error",e)

time.sleep(5)



##pause the video
if 'paused' in video_element.get_attribute('class'):
    video_element.click()  # Play the video
else:
    video_element.click()  # Pause the video

time.sleep(5)


## go back to main page

driver.switch_to.default_content()

### go back

driver.find_element(By.XPATH,"//button[@aria-label='Go Back and continue playing video']").click()

time.sleep(5)



###logout

driver.find_element(By.XPATH,"//button[@id='signOutSideBar']").click()

time.sleep(5)

driver.quit()