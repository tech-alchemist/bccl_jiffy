#!/usr/bin/env python
## AutoLogin Utility BCCL (Times Group) Jiffy ##
## Author : ABhishek Rana ##

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, pickle, configparser, sys , base64

# Check Argument #
try:
    trgr = sys.argv[1].lower()
except:
    print("[ERROR] Argument missing")
    print("Usage : python",sys.argv[0],"<in/out>")
    exit()

# Load Config #
cp = configparser.ConfigParser()
cp.read('config.ini')

link = (cp["jiffy"]["link"])
user = (cp["jiffy"]["user"])
bpwd = (cp["jiffy"]["pass"])
b641 = bpwd.encode("ascii")
b642 = base64.b64decode(b641)
pswd = b642.decode("ascii")
#print(link, user , pswd)

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get(link)

assert "Timescape" in driver.title

# SignIn to Jiffy #
driver.implicitly_wait(5)  #in seconds
box1 = driver.find_element("xpath", '//*[@id ="email" and @name="emailid"]')
box1.send_keys(user)
box2 = driver.find_element('xpath', '//*[@id ="password" and @name="password"]')
box2.send_keys(pswd)
btn = driver.find_element('xpath', '//*[@class ="btn btn-primary" and text()="Sign In"]')
btn.click()

if trgr == "in":
    # Either Check In #
    btn = driver.find_element('xpath', '//*[@class ="btn btn-left activeSwipe"]')
    btn.click()
elif trgr == "out":
    # Or CheckOut #
    btn = driver.find_element('xpath', '//*[@class ="btn btn-left activeSwipe"]')
    btn.click()
else:
    print("[ERROR] Wrong Argument -> ",sys.argv[1])
    print("Usage : python",sys.argv[0],"<in/out>")

# Logout Jiffy #
driver.implicitly_wait(5)  #in seconds
btn = driver.find_element('xpath', '//*[@class ="menu-toggle-ic"]')
btn.click()
btn = driver.find_element('xpath', '//*[@class ="fa fa-sign-out"]')
btn.click()
driver.implicitly_wait(5)  #in seconds
driver.close()
## E O F ##
