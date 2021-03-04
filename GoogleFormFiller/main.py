from selenium import webdriver
from datetime import datetime
import schedule
import time

def checkin():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_argument("--headless")
    option.add_argument("disable-gpu")
    option.add_experimental_option("excludeSwitches", ['enable-automation']);

    browser = webdriver.Chrome(executable_path='/users/hongjunyun/chromedriver', options=option)

    browser.get("https://forms.gle/LLUCAY2GEoyAAL4m9")

    date = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    submitbutton = browser.find_elements_by_class_name("freebirdThemedFilledButtonM2")

    date[0].send_keys(datetime.today().strftime('%Y-%m-%d'))

    radiobuttons[0].click()

    submitbutton[0].click()

    print("Task Complete!")

schedule.every().day.at("10:01").do(checkin)

while True:
    schedule.run_pending()
    time.sleep(30)