from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

from GetContacts import phno,names

chrome = webdriver.Chrome("INSERT CHROME DRIVER'S PATH")

wait = WebDriverWait(chrome,600)

chrome.get('https://contacts.google.com/?hl=en/')

print("Please login with your google account")

time.sleep(5.0)

for i in range(len(names)):
    x_new_contact = '//button[@title="Add new contact"]'
    new_contact = wait.until(ec.presence_of_element_located((By.XPATH, x_new_contact)))
    new_contact.click()

    x_name = '//input[@aria-label="First name"]'
    name = wait.until(ec.presence_of_element_located((By.XPATH, x_name)))
    name.send_keys("A1" + names[i])

    x_ph = '//input[@aria-label="Phone"]'
    ph = wait.until(ec.presence_of_element_located((By.XPATH, x_ph)))
    ph.send_keys(phno[i])

    x_save = '//button[@jsname="x8hlje"]'
    save = chrome.find_element_by_xpath(x_save)
    save.click()

    time.sleep(1.5)
    x_close = '#yDmH0d > div.llhEMd.iWO5td > div > div.g3VIld.G2PfHe.Up8vH.Whe8ub.hFEqNb.J9Nfi.iWO5td > content > div > div.KEUMte > div > div.bLQjSd.mBvP5e > div:nth-child(4) > svg > path:nth-child(2)'
    close = chrome.find_element_by_css_selector(x_close)
    close.click()

    time.sleep(1)