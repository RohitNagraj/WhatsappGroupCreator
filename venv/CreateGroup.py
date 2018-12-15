from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from GetContacts import names

groupName = "GROUP NAME HERE"

chrome = webdriver.Chrome("INSERT CHROME DRIVER'S PATH")

wait = WebDriverWait(chrome,600)

chrome.get('https://web.whatsapp.com/')

x_menuButton = '//div[@title="Menu"]'
menuButton = wait.until(ec.presence_of_element_located((By.XPATH, x_menuButton)))
menuButton.click()

x_newGroup = '//div[@title="New group"]'
newGroup = wait.until(ec.presence_of_element_located((By.XPATH, x_newGroup)))
newGroup.click()

x_name = '//input[@class="_16RnB copyable-text selectable-text"]'
nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_name)))
for i in names:
    nameField.send_keys('A1' + i)
    nameField.send_keys(Keys.ENTER)


nameField.send_keys(Keys.ENTER)

x_group = '//div[@class="_2S1VP copyable-text selectable-text"]'
nameField = wait.until(ec.presence_of_element_located((By.XPATH,x_group)))
nameField.send_keys(groupName + Keys.ENTER)