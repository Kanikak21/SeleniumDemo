from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get('https://app.hubspot.com/login')



explicit_wait= WebDriverWait(driver,20)

explicit_wait.until(EC.title_is('HubSpot Login'))

print(driver.title)
email_id = explicit_wait.until(EC.presence_of_element_located((By.ID,'username')))  
email_id.send_keys('knk204@gmail.com')

time.sleep(10)