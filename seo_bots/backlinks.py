from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\H5SH\other\projects\seo_bots\chromedriver-win32\chromedriver.exe')

websites= [
    'https'
]

backlink = 'https://heic2any1.com/'
message = f"Check out the easy and fast way to convert your heic images: {backlink}"

def post_backlink(url):
    driver.get(url)
    time.sleep(3)

    comment_box = driver.find_element(By.XPATH,'//textarea[@id="comment"]')
    comment_box.send_keys(message)

    submit_button = driver.find_element(By.XPATH, '//button[@id="submit-comment"]')
    submit_button.click()

    time.sleep(2)

for site in websites:
    post_backlink(site)

driver.quit()
