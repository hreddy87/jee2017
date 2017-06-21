import os
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.support.ui import WebDriverWait


"""importing required modules<close>"""

"""setting up chromedriver for selenium<open>"""

#1.set the location of the chromedriver manually[used in 2. and 3.]
chromedriver = "C:/Users/harshith reddy/Desktop/dev/chromedriver.exe"

#2.setting up the chromedriver so as to prevent certificate error and full screen
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--test-type")
#chrome_options.add_argument("--kiosk")

#3 to solve not in os path error
os.environ["webdriver.chrome.driver"] = chromedriver

"""setting up chromedriver for selenium<close>"""

def evaluate(s):
    global driver
    eval(s)

def multick(string):
    global driver
    global file
    for n in range(1000):
        try:
            evaluate(string)
        except:
            continue
        return
    file.close()

driver=webdriver.Chrome(chromedriver,chrome_options=chrome_options)
driver.get("http://iitjeetoppers.com/")
time.sleep(2)
html=BeautifulSoup(driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML"),"html.parser")
file = open(r"C:/Users/harshith reddy/F1itjeeAdvanced2017.csv", "w")
for i in range(42):
    
    li=html.find("ul",{"class":"list-unstyled centrelinks"}).findAll("a")
    xpath='//*[@id="'+li[i].attrs["id"]+'"]'
    multick("driver.find_element_by_xpath('//*[@id=\"theme-panel\"]/a/img').click()") 
    multick(r"driver.find_element_by_xpath(xpath).click()")
    multick(r"driver.find_element_by_partial_link_text('and').click()")
    multick(r"driver.find_element_by_partial_link_text('Last').click()")
    time.sleep(2)
    html=BeautifulSoup(driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML"),"html.parser")
    table=html.find("table",{"rules":"all"}).findAll("td")
    last_rank=re.sub(r"( ){2,}"," ",table[-1].getText().replace("\n"," ")).strip()
    multick(r"driver.find_element_by_partial_link_text('First').click()")
    last_rank_page=None
    while True :
        time.sleep(2)
        html=BeautifulSoup(driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML"),"html.parser")
        table=html.find("table",{"rules":"all"}).findAll("td")
        last_rank_page=re.sub(r"( ){2,}"," ",table[-1].getText().replace("\n"," ")).strip()
        
        sum=0
        for t in table:
            sum = sum + 1
            if sum % 5 == 0:
                file.write(re.sub(r"( ){2,}"," ",t.getText().replace("\n"," ")).strip()+"\n")
            else:
                file.write(re.sub(r"( ){2,}"," ",t.getText().replace("\n"," ")).strip()+ ",")
        
        if last_rank==last_rank_page:
            print(100)
            break
        
        multick(r"driver.find_element_by_partial_link_text('Next').click()")
file.close()
        
	
	
