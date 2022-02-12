import time
import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import service, Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By


# Give browser up to 30 seconds to respond
driver.implicitly_wait(30)

# create a Chrome driver instance, specify path to chromedriver file
driver = webdriver.Chrome()
s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)

# Navigate to Wikipedia app website
driver.get('https://www.wikipedia.org/')


# maximize the window

driver.maximize_window()


# Check that Wikipedia URL and the home page title are displayed

if driver.current_url != 'https://www.wikipedia.org/' or driver.title != 'Wikipedia':
    print(f'Wiki did not launch. Check your code or application!')
    print(f'Current URL: {driver.current_url} Page Title: {driver.title}')

else:
    print('Hurray! Wikipeadia Launched Successfully')
    print(f'Wikipedia homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
sleep(2)

#In a search field, find Python (programming language) and click on it.

search_box = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/div/input')
search_box.send_keys('Python (programming language)')
sleep(2)

# Check that the title Python (programming language) is displayed.

search_button = driver.find_element(By.XPATH, '/html/body/div[3]/form/fieldset/button/i')
search_button.click()
sleep(2)

#  Click by the Wikipedia main image (logo) to navigate back to the home page and close the browser.

search_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/a')
search_button.click()

sleep(2)
driver.quit()
