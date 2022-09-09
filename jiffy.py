#!/usr/bin/env python
## AutoLogin Utility BCCL (Times Group) Jiffy ##
## Author : Abhishek Rana ##

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, pickle, configparser, sys , base64 , pytz , requests

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
mail = (cp["jiffy"]["mail"])
bpwd = (cp["jiffy"]["pass"])
b641 = bpwd.encode("ascii")
b642 = base64.b64decode(b641)
pswd = b642.decode("ascii")
#print(link, mail)
tgtkn = (cp["telegram"]["Bot_tkn"])
tgcid = (cp["telegram"]["Chat_ID"])
user = mail.split("@")[0]

# Install Driver
s=Service(ChromeDriverManager().install())
opts = webdriver.ChromeOptions()

# Custom Browser Options #
opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--window-size=1920,1080")
opts.add_argument('ignore-certificate-errors')
opts.add_experimental_option("excludeSwitches", ["enable-automation"])
prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
opts.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=s,options=opts)
driver.maximize_window()

def timer(msg):
    IST = pytz.timezone('Asia/Kolkata')
    dist = datetime.now(IST)
    return(dist.strftime("[Jiffy] %a %e%b%Y @ %l:%M:%S %p "+msg))

def PostTG(tkn,cid,msg):
    requests.packages.urllib3.disable_warnings()
    turl = f'https://api.telegram.org/bot{tkn}/sendMessage'
    tdat = {'chat_id': cid, 'text': msg}
    try:
        resp = requests.post(turl, tdat , verify=False)
        print("[+] TG Channel Push = "+str(resp.status_code))
    except:
        print("[-] Failed, TG push with provided ids, check credentials.")
        pass

# Open Jiffy
driver.get(link)
assert "Timescape" in driver.title

# SignIn to Jiffy #
driver.implicitly_wait(5)  #in seconds
box1 = driver.find_element("xpath", '//*[@id ="email" and @name="emailid"]')
box1.send_keys(mail)
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
        msg="[🟢 ⬇️ IN]"+user
        tmsg=timer(msg)
        print(tmsg)
        PostTG(tgtkn, tgcid, tmsg)
    except:
        msg="[🔴 ⬇️ IN] "+user
        tmsg=timer(msg)
        print(tmsg)
        PostTG(tgtkn, tgcid, tmsg)
        pass
elif trgr == "out":
    # Or CheckOut #
    try:
        btn = driver.find_element('xpath', '//*[@class ="btn btn-right activeSwipe"]')
        btn.click()
        driver.implicitly_wait(5)
        msg="[🟢 ⬆️ OUT]"+user
        tmsg=timer(msg)
        print(tmsg)
        PostTG(tgtkn, tgcid, tmsg)
    except:
        msg="[🔴 ⬆️ OUT]"+user
        tmsg= timer(msg)
        print(tmsg)
        PostTG(tgtkn, tgcid, tmsg)
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

