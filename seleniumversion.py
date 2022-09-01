# -*- coding: utf-8 -*-
# from pyuseragents import random as random_useragent
from selenium import webdriver
import time


from selenium.common.exceptions import NoSuchElementException

import TG
import threading

from selenium.webdriver.common.by import By


# randomUserAgent = random_useragent()
# options = webdriver.ChromeOptions()
# options.add_argument(randomUserAgent)
# driver = webdriver.Chrome(executable_path='C:\\Users\\larso\\PycharmProjects\\discord giveaway winner\\chromedriver.exe', options=options)
# driver.add_cookie({'accept': '*/*', 'accept-language': 'ru,en;q=0.9,vi;q=0.8,es;q=0.7'})

def check_doctor_tickets():
    # randomUserAgent = random_useragent()
    options = webdriver.ChromeOptions()
    # options.add_argument(randomUserAgent)
    driver = webdriver.Chrome(
        executable_path='C:\\Users\\larso\\PycharmProjects\\discord giveaway winner\\chromedriver.exe', options=options)
    while True:
        try:
            driver.get("""https://gorzdrav.spb.ru/service-free-schedule#[{"district":"4"},{"lpu":"296"}]""")
        except Exception as e:
            TG.signal_myTG("Что-то не так : " + e)
        else:
            time.sleep(15)
            try:
                element = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[12]/div[3]/div[3]/div/div[1]/div[16]")
                element = element.find_element(By.CLASS_NAME, "service-speciality__tickets")
                TG.signal_myTG("Появились номерки : " + element.text)
                time.sleep(60)
            except NoSuchElementException:
                TG.signal_myTG("Пока номерков нет")
                time.sleep(1200)
            except Exception as e:
                TG.signal_myTG("Ошибка : " + e)
                time.sleep(300)
                driver.refresh()
                time.sleep(15)


thread1 = threading.Thread(target=check_doctor_tickets).start()
