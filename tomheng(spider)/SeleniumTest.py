from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import json

with open('data.json', 'r',encoding="utf-8") as f:
    data = json.load(f)

PATH = "./driver/chromedriver.exe"
#user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
option = webdriver.ChromeOptions()
#option.add_experimental_option("excludeSwitches",['enable-automation','enable'])
#option.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome(PATH,options=option)

driver.get("https://isw.um.edu.mo/siapp/faces/home")

userName = driver.find_element(By.CSS_SELECTOR,'#userNameInput')
userName.send_keys(f"{data['username']}")

password = driver.find_element(By.CSS_SELECTOR,'#passwordInput')
password.send_keys(f"{data['password']}")

submit = driver.find_element(By.CSS_SELECTOR,"#submitButton")
submit.click()

#Error exception and 2FA
try:
    error = driver.find_element(By.CSS_SELECTOR,"#errorText")
    print("用戶名或密碼不正確。請鍵入正確的用戶名和密碼，並重試。")
except:
    print("登入成功")

time.sleep(10)
driver.quit()