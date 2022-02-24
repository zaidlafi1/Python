from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas

import time

browser = webdriver.Chrome(executable_path='/home/zaid/Downloads/chromedriver_linux64/chromedriver')
# open openhook web
# browser = webdriver.Chrome('/home/zaid/Downloads/chromedriver_linux64/chromedriver')

browser.set_window_size(1024, 600)
browser.maximize_window()
browser.get('https://zaid.elevatus.io/')
wait = WebDriverWait(browser, 3)
# login using phone number


browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/i').click()
time.sleep(3)

element0 = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[2]/div[2]/div[1]/a').click()
time.sleep(3)

username = browser.find_element_by_xpath('//*[@id="__next"]/div[4]/div/div/div/div/a[1]/div/div/div[2]/button').click()
# username.send_keys('0700888866')
# username.send_keys(Keys.ENTER)
time.sleep(3)
pas = browser.find_element_by_xpath('//*[@id="__next"]/div[3]/div/div[2]/div/div[7]/button').click()

element1 = browser.find_element_by_xpath('//*[@id="header"]/div/div[1]/a').click()
time.sleep(3)
