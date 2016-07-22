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

mySelect = Select(browser.find_element_by_id("searchscope"))
mySelect.select_by_value("98")

Submit = browser.find_element_by_xpath("id('search')/span[3]/input")
Submit.click()  

browser.implicitly_wait(400) 

# By Author search 

SearchAuthor = browser.find_element_by_link_text("By Author") 
SearchAuthor.click()

assert "Author Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("shakespeare") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Newest First")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("19")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)

# By Title

SearchTitle = browser.find_element_by_link_text("By Title") 
SearchTitle.click()  

assert "Title Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("merchant") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Oldest First")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("18")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)

# By Journal Title 

SearchJournal = browser.find_element_by_link_text("By Journal Title") 
SearchJournal.click()  

assert "Journal Title Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("wall street journal") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Title")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("7")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)


# By Subject

SearchSubject = browser.find_element_by_link_text("By Subject") 
SearchSubject.click()  

assert "Subject Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("United States History Civil War") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Author")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("48")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)

#By Genre 

SearchSubject = browser.find_element_by_link_text("By Genre") 
SearchSubject.click()  

#assert "Genre Search" in browser.page_source

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("fantasy fiction") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Format")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("74")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)

#By Isbn 

SearchSubject = browser.find_element_by_link_text("By ISBN") 
SearchSubject.click()  

assert "ISBN/ISSN Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("9780471793717") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("System Sorted")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("1")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)

#By Call number  
  
SearchSubject = browser.find_element_by_link_text("By Call number") 
SearchSubject.click()  

assert "Call Number Search" in browser.page_source 

Search = browser.find_element_by_id("SEARCH") 
Search.send_keys("jfe 84 1003") 

Selectsort = Select(browser.find_element_by_id("sortdropdown"))
Selectsort.select_by_visible_text("Call Number")  

Selectcollection = Select(browser.find_element_by_id("searchscope")) 
Selectcollection.select_by_value("98")

SubmitAuthor = browser.find_element_by_xpath("id('rightSideCont')/div[2]/form/span/a/img") 
SubmitAuthor.click()

browser.implicitly_wait(400)  

print("\t\t\t\t\n")
print("Successfully executed the Automatic test cases for:\t")
print("1) Keyword Search\t")
print("2) Author Search\t")
print("3) Title Search\t")
print("4) Journal Title Search\t")
print("5) Subject Search\t")
print("6) Genre Search\t")
print("7) ISBN Search\t")
print("8) Call Number Search\t")