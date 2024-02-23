from selenium import webdriver
from selenium.webdriver.common.by import By
import time



options= webdriver.ChromeOptions()
options.add_argument("--headless")
driver= webdriver.Chrome(options=options)

driver.implicitly_wait(5)

driver.get("https://www.rediff.com/")
print(driver.title)
# driver.find_element(By.NAME,'q').send_keys("PGWP Canada")
# searchoptions= driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e>li>div>div:nth-child(2)>div>div:nth-child(1)>span")

# for ele in searchoptions:
    
#     print(ele.text)

#     if ele.text =='pgwp canada meaning':
#         ele.click()
#         break

# print(driver.find_element(By.XPATH, '//*[@id="sBQTL"]/div[1]/span').text)
# assert True== driver.find_element(By.XPATH, '//*[@id="sBQTL"]/div[1]/span').is_displayed()
# driver.find_element(By.XPATH, '//*[@id="sBQTL"]/div[1]/span').click()


time.sleep(5)

# visible area
# driver.get_screenshot_as_file("screenshot.png")

S =lambda X: driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot("full.png")

# to release the driver instance from memory
driver.quit()