from pyuseragents import random as random_useragent
from selenium import webdriver
import time
import TG

from selenium.webdriver.common.by import By

randomUserAgent = random_useragent()
options = webdriver.ChromeOptions()
options.add_argument(randomUserAgent)
driver = webdriver.Chrome(executable_path='C:\\Users\\larso\\PycharmProjects\\chromedriver.exe', options=options)
# driver.add_cookie({'accept': '*/*', 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7'})
driver.get("https://opensea.io/collection/car-tooned")
while True:
    try:
        numOfCars = driver.find_element(By.ID, 'main').text.split('\n')[3]
        if numOfCars == '29':
            TG.signal_myTG_silent("Still 29")
            time.sleep(300)
        else:
            TG.signal_myTG(f'NEW CARS = {numOfCars}')
            time.sleep(15)
        driver.refresh()
    except Exception as e:
        TG.signal_myTG_silent(e)
        #print()
