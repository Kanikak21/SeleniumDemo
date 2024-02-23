from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.hubinternational.com/en-CA/contact-us/personal-insurance/")
# print(driver.title)

Fname= driver.find_element(By.XPATH,'//*[@id="CrmItem_FirstNameField"]')
driver.execute_script("document.getElementById('CrmItem_FirstNameField').value='Kanika'",Fname)
title= driver.execute_script("return document.title;")
print(title)

driver.execute_script("history.go(0);")
# driver.execute_script("alert('Welcome to Hub International');")

inner_text= driver.execute_script("return document.documentElement.innerText")
print(inner_text)

# form = driver.find_element(By.XPATH,'//*[@id="generalContactForm"]/section[2]/div/div/div/div')
# driver.execute_script("arguments[0].style.border= '3px solid red'",form)

# to scroll to bottom of the page
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# Phone= driver.find_element(By.XPATH,'//*[@id="CrmItem_PhoneField"]')
# driver.execute_script("arguments[0].scrollIntoView(true);", Phone)

print(driver.execute_script("return navigator.userAgent;"))
time.sleep(5)