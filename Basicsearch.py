from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

# Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

# Goto to browser 
browser.get("http://browse.nypl.org")  

browser.implicitly_wait(20)

#library = browser.find_element_by_xpath("//*[@id='rightSideCont']/p[3]/a") 
#library.click()

# Basic Search 

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.send_keys("Software Testing")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()  

#Title 

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.clear()
searchString.send_keys("testing across the entire software development life cycle / Gerald D. Everett, Raymond McLeod, Jr.")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()

#Isbn number  

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.clear()
searchString.send_keys("9780471793717")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click() 

#Author 
browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.clear()
searchString.send_keys("Everett, Gerald D.")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click() 

#Research  number

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString") 
searchString.clear()
searchString.send_keys("JSE 07-859")

#Searchbutton 

browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()

print("\t\t\t\t\n")
print("Successfully executed the Automatic test cases for:\t")
print("1) Keyword Search\t")
print("2) Title Search\t")
print("3) ISBN Search\t")
print("4) Author Search\t")
print("5) Research number Search\t")







