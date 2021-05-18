# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:14:01 2021
@author: roscibely
"""

import time                                                                 # to let the program sleep 
from selenium import webdriver                                              # import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = 'C:\Program Files (x86)\chromedriver.exe'                            # path to chromedriver.exe 
driver = webdriver.Chrome(path)                                             # create nstance of webdriver
url = 'http://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar' # Lattes url
driver.get(url)                                                             # Code to open a specific url
keyword = 'rosana cibely'                                                   # set the name you want to search for
check = driver.find_element_by_id('buscarDemais').click()                   # clik on the box
searchBar = driver.find_element_by_name('textoBusca')                       # we find the search bar using it's name attribute value
searchBar.send_keys(keyword)                                                # first we send our keyword to the search bar followed by the enter \n key
searchBar.send_keys('\n')
time.sleep(10)                                                              # wait

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "resultado")))                     # wait for search results to be fetched
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Rosana Cibely Batista Rego"))).click() # contains the search results
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Abrir Currículo"))).click()            # open the cv window
    time.sleep(10)                                                                                                    # wait
    newURl = driver.window_handles[1]                                                                                 # get the url of the new window 
    driver.switch_to.window(newURl)                                                                                   # update the url 
    element = driver.find_element_by_class_name("informacoes-autor").text                                             # get the information
    print(element[70:-1])                                                                                             # print the information
except Exception as e:
    print(e)
    driver.quit()
