import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from testePro.testepro import driver

driver = webdriver.Chrome()  #Drive do navegador

driver.get("https://web.whatsapp.com/") # Acessando o whatsap

while len(driver.find_element(By.XPATH, ' '))< 1:
    input()
    pass
