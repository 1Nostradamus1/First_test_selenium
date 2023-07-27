from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# скрипт заходит в вк, вводит телефон и пароль
s = Service(executable_path="C:\chromedriver")
driver = webdriver.Chrome(service=s)
try:
    driver.maximize_window()
    driver.get("https://www.vk.com/")
    time.sleep(5)

    phone_Input = driver.find_element(By.ID, "index_email")
    phone_Input.clear()
    phone_Input.send_keys("88005553535")
    phone_Input.send_keys(Keys.ENTER)
    time.sleep(5)
    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys("password1234")
    time.sleep(5)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
