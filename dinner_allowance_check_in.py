from selenium import webdriver
import time

"""
using webdriver to login a website and press check_in button
"""

# browser without window
opt = webdriver.ChromeOptions()
opt.headless = True
browser = webdriver.Chrome(options=opt)

browser.get('https://login.XXXX.com')

# input your username and password
browser.find_element('name', 'username').send_keys(' your username ')
browser.find_element('name', 'password').send_keys(' your password ')

# click the login button
browser.find_element('id', 'loginBtn').click()
time.sleep(1)

# open the dinner allowance page
browser.get('the website you press the check_in button')

# find the xpath and click the button
press_button = browser.find_element('xpath', '/html/body/div[2]/div[3]/button[1]')
time.sleep(1)
press_button.click()

time.sleep(2)
# quit webdriver with or without your message
print('-----------Done! have fun now > < -------------')
browser.quit()
