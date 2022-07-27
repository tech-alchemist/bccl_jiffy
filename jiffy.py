#!/usr/bin/env python
## AutoLogin Utility BCCL (Times Group) Jiffy ##
## Author : Abhishek Rana ##

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, pickle, configparser, sys , base64

# Check CLI Arguments #
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
#print(link, user)

# Install Driver
s=Service(ChromeDriverManager().install())
opts = webdriver.ChromeOptions()

# Custom Browser Options #
opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
opts.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
opts.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=s,options=opts)
driver.maximize_window()

# Open Jiffy
driver.get(link)
assert "Timescape" in driver.title

# SignIn to Jiffy #
driver.implicitly_wait(5)  #in seconds
box1 = driver.find_element("xpath", '//*[@id ="email" and @name="emailid"]')
box1.send_keys(user)
box2 = driver.find_element('xpath', '//*[@id ="password" and @name="password"]')
box2.send_keys(pswd)
btn = driver.find_element('xpath', '//button[@class ="btn btn-primary"]')
try:
    btn.click()
except:
    print("[*] Click was not required, Skipped initial Sign In button")
    pass

if trgr == "in":
    # Either Check In #
    try:
        btn = driver.find_element('xpath', '//*[@class ="btn btn-left activeSwipe"]')
        btn.click()
        driver.implicitly_wait(5)
        print("[*] Marked [Checked In] @ Jiffy")
    except:
        print("[!] You've already Checked In @ Jiffy")
        pass
elif trgr == "out":
    # Or CheckOut #
    try:
        btn = driver.find_element('xpath', '//*[@class ="btn btn-left activeSwipe"]')
        btn.click()
        driver.implicitly_wait(5)
        print("[*] Marked [Checked Out] @ Jiffy")
    except:
        print("[!] You've already Checked Out @ Jiffy")
        pass
else:
    print("[ERROR] Wrong Argument -> ",sys.argv[1])
    print("Usage : python",sys.argv[0],"<in/out>")

# Logout Jiffy #
btn = driver.find_element('xpath', '//*[@class ="menu-toggle-ic"]')
btn.click()
btn = driver.find_element('xpath', '//*[@class ="fa fa-sign-out"]')
btn.click()
driver.implicitly_wait(5)  #in seconds
driver.close()
## E O F ##



