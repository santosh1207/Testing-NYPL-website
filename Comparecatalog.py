from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import Select 
import time

#Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

#Goto to browser  
#Catalog.nypl.org catalog page 
browser.get("https://catalog.nypl.org/")  

assert "New York Public Library Catalog" in browser.title
browser.implicitly_wait(20) 

#catalog search 

#By Keyword search 

Keyword = browser.find_element_by_link_text("By Keyword") 
Keyword.click() 

assert "Keyword Search" in browser.page_source		

Searchkeyword = browser.find_element_by_id("SEARCH") 
Searchkeyword.send_keys("Design")

Submit = browser.find_element_by_xpath("id('search')/span[3]/input")
Submit.click()  

browser.implicitly_wait(200) 

# By Author search 

SearchAuthor = browser.find_element_by_link_text("By Author") 
SearchAuthor.click() 

assert "Author Search" in browser.page_source  

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("shakespeare") 

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(200)

# By Title

SearchTitle = browser.find_element_by_link_text("By Title") 
SearchTitle.click()  

assert "Title Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("merchant") 

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(200)

# Browse.nypl.org catalog page 

browser.get("http://browse.nypl.org")  

browser.implicitly_wait(20)

#By Keyword search 

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.send_keys("Design")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()  

#By Author search 

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.clear()
searchString.send_keys("shakespeare")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()

#By Title

browser.implicitly_wait(20)
searchString = browser.find_element_by_id("searchString")
searchString.clear()
searchString.send_keys("merchant")

#Searchbutton 
browser.implicitly_wait(20)
Searchbutton = browser.find_element_by_id("searchImageSumbitComponent")
Searchbutton.click()

print("Successfully compared the two websites by searching common searches in both sites and viewing the outputs")