from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv, os

listKeyword=[]  # list in which it is storage all keywords from file "dataTask2.txt"



filepath="dataTask2.txt" # file in which it is storage keywords to use in the browser 
f=open(filepath,"r")     # open file


for line in f:              #read file line per line      
	x=line.strip('\n')  #remove new line between keywords
	listKeyword.append(x) # add any keywors to list

f.close()   #close file


def loopTag(links): #function which will be looking for all links by keyword in the browser
    listLink=[]
    for lnk in links:
        lnk2=str(lnk.get_attribute("href"))
        if "https://www.searchenginejournal.com/" in lnk2 and "google.com" not in lnk2 and "webcache.googleusercontent.com" not in lnk2: #condition to get links only from searchenginejournal.com
            listLink.append(lnk2) # here found links are adding to list
            
    return listLink

driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver", quiet=False)  #path and option to launch Safari browser 

driver.get("http://google.com")  # here it is set page to open



agree = driver.find_element_by_id("L2AGLb") #find element HTML (it is button to accept privacy rules)
agree.click() # click on the found button


for keyword in listKeyword: #loop for every keyword included in file dataTask2.txt
    
    text_area = driver.find_element_by_name("q")  #looking for element HTML in the search engine
    text_area.send_keys(f"site:https://www.searchenginejournal.com/ {keyword}") #typing in search engine keyword
    text_area.send_keys(Keys.ENTER) # sending to search engine ENTER as simulation physical key ENTER
    time.sleep(2) #wait 2 second

    links=driver.find_elements_by_tag_name("a") #looking for all tag HTML in source code
    with open('linksTask2.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f) # set write data in csv
        writer.writerow(loopTag(links)) # typing found links to file linksTask2.csv

    results=driver.find_element_by_id('result-stats')  #looking for all element HTML by id in source code
    with open('results.txt', 'a', encoding='UTF8') as f:
        f.write(str(keyword) + " - " + str(results.text) + "\n") # typing keyword and total numbers of results to file results.txt
    
        
        
## Below there is handling exceptions. It is checking if Page 2 exist.
    try:
        page2=driver.find_element_by_xpath('//*[@id="xjs"]/table/tbody/tr/td[3]/a')    #looking for page 2  in  source code
        time.sleep(2)
        if page2.get_attribute("aria-label") == "Page 2": #  if found element HTML equal "Page 2", next steps are the same like above. Links are typing to file linksTask2.csv
                                                           # and number of results to file results.txt
            page2.click()
            time.sleep(2)

            links=driver.find_elements_by_tag_name("a")
            with open('linksTask2.csv', 'a', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(loopTag(links))

            results=driver.find_element_by_id('result-stats')
            with open('results.txt', 'a', encoding='UTF8') as f:
                f.write(str(keyword) + " - " + str(results.text) + "\n")
    except:
        print("Page 2 doesn't exist")           # if Page doesn't exist, it prints information




        

 
    
    

