from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver= webdriver.Chrome()
driver.implicitly_wait(20)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)
# driver.find_element(By.ID,"Form_getForm_subdomain").send_keys("knk204")
driver.find_element(By.CSS_SELECTOR,"#Form_getForm_subdomain").send_keys("knk204")
print(driver.find_element(By.CSS_SELECTOR,'#recaptcha-anchor-label > span').text)

#recaptcha-anchor-label > span
# driver.find_element(By.LINK_TEXT,'Solutions').click()
driver.find_element(By.XPATH,'/html/body/nav/div/a/img').click()


time.sleep(5)