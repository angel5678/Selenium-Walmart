from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(chrome_options=options, executable_path=PATH)

driver.get("https://www.walmart.co.cr/")

while True:
    time.sleep(1)