from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


file_to_upload = 'C:\\H5SH\\other\\projects\\seo_bots\\1.heic'
download_dir = 'C:\H5SH\other\projects\seo_bots'
url = 'https://heic2any1.com/'

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('prefs', {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options, executable_path='C:\H5SH\other\projects\seo_bots\chromedriver-win32\chromedriver.exe')

def delete_latest_file(download_dir):
    files = os.listdir(download_dir)
    paths = [os.path.join(download_dir, basename) for basename in files if basename.endswith('.zip')]
    if len(paths) > 0:
        os.remove(paths[0])
    
def upload_and_download():

    upload_element = driver.find_element(By.XPATH, '//input[@type="file"]')
    upload_element.send_keys(file_to_upload)

    submit_button = driver.find_element(By.XPATH, '//button[@id="submit-upload"]')
    submit_button.click()

    time.sleep(10)

    delete_latest_file(download_dir)

# Open the site and wait for load
driver.get(url)
time.sleep(3)

while(True):
    upload_and_download()