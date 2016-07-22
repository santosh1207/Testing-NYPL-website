from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select 
import time
import random

import random

#ran = random.randint(1,50) 
#ran1 = "test+@ran"
#print ran1

#Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

#Goto to browser 
browser.get("https://catalog.nypl.org/")  

assert "New York Public Library Catalog" in browser.title
browser.implicitly_wait(20) 

#Email Updates 

Subscribe = browser.find_element_by_xpath("//*[@id='SubscribeButton']/span[1]")
Subscribe.click()

assert "Subscription Center | The New York Public Library" in browser.title

Emailaddress = browser.find_element_by_name("Email Address") 
Emailaddress.send_keys("test01@gmail.com") 

Selectsort = Select(browser.find_element_by_id("Preferred Location"))
Selectsort.select_by_index("2")  

browser.find_element_by_xpath("id('subscribeForm')/table/tbody/tr[11]/td[2]/input").click()  

assert "Thank You! | The New York Public Library" in browser.title
print("Successfully tested email Subscription")