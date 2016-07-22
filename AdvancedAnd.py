from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time
# Navigate to chrome
options = webdriver.ChromeOptions() 
options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=options) 

# Goto to browser 
browser.get("https://catalog.nypl.org/")  

library = browser.find_element_by_xpath("//*[@id='rightSideCont']/p[3]/a") 
library.click()

# Using And 

Advancedsearch = browser.find_element_by_id("advancedSearchLinkComponent") 
Advancedsearch.click() 

#first Row 

Selecttype0 = Select(browser.find_element_by_id("searchType_0"))
Selecttype0.select_by_visible_text("Title") 
			
search_box0 = browser.find_element_by_xpath("//input[@name='searchTerm_0']") 
search_box0.send_keys("Software testing")


#Second Row 

Selecttype1 = Select(browser.find_element_by_id("searchType_1"))
Selecttype1.select_by_visible_text("Author") 
			
search_box1 = browser.find_element_by_id("searchTerm_1") 
search_box1.send_keys("Everett, Gerald D.")


SelectLang = Select(browser.find_element_by_id("limitValue_3"))
SelectLang.select_by_value("eng") 
		
startYear = browser.find_element_by_id("startYear")
startYear.send_keys("1900") 

EndYear = browser.find_element_by_id("endYear")
EndYear.send_keys("2014")


Clicksearch = browser.find_element_by_id("searchSubmit").click()

print("Successfully implemented Advanced Search with using AND boolean value")
