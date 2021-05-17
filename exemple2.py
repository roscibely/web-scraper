from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe') # create instance of webdriver
driver.get('https://www.google.com')                                 # open google url
keyword = 'AI'                                                       # set the keyword you want to search for
searchBar = driver.find_element_by_name('q')                         # we find the search bar using it's name attribute value
searchBar.send_keys(keyword)                                         # first we send our keyword to the search bar followed by the enter \n
searchBar.send_keys('\n')
time.sleep(5)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
