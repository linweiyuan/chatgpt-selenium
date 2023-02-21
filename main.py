import json
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from undetected_chromedriver import Chrome, ChromeOptions

options = ChromeOptions()
# options.add_argument("--proxy-server=socks5://127.0.0.1:20170")
# options.add_argument("--headless")

driver = Chrome(options=options)

driver.get('https://chat.openai.com')
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

wait = WebDriverWait(driver, 60)

wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'btn.flex.justify-center.gap-2.btn-primary'))).click()
wait.until(EC.presence_of_element_located(
    (By.ID, 'username'))).send_keys(username)
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'button[type=submit]'))).click()
wait.until(EC.presence_of_element_located(
    (By.ID, 'password'))).send_keys(password)
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, 'button[type=submit]'))).click()

driver.get("https://chat.openai.com/api/auth/session")
plain_text = driver.execute_script("return document.body.innerText")
json_data = json.loads(plain_text)
access_token = json_data["accessToken"]

print(access_token)

driver.quit()
