"""importing required modules<open>"""

import os
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

"""importing required modules<close>"""

"""setting up chromedriver for selenium<open>"""

#1.set the location of the chromedriver manually[used in 2. and 3.]
chromedriver = "C:/Users/harshith reddy/Desktop/dev/chromedriver.exe"

#2.setting up the chromedriver so as to prevent certificate error
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--test-type")

#3 to solve not in os path error
os.environ["webdriver.chrome.driver"] = chromedriver

"""setting up chromedriver for selenium<close>"""


class FitjeeRankListRetriever:

    def __init__(self,link,chromedriver=chromedriver,chrome_options=chrome_options):

        self.page=1
        self.driver=webdriver.Chrome(chromedriver,chrome_options=chrome_options)
        self.driver.get(link)
        self.present_html=self.driver.page_source




    def next(self):
        flag = 0
        for i in range(10000):

            try:
                self.driver.find_element_by_link_text("Next").click()

            except:
                continue
            flag = 1
            break

        if flag==1:
            self.page+=1
        else:
            raise Exception("Button not found")
        time.sleep(2)


        self.present_html=self.driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")



instant=FitjeeRankListRetriever("http://jeemain.iitjeetoppers.com/2017/CompleteResult2017.aspx")
sum=0

#filelocation where you want to store the csv
file = open(r"C:/Users/harshith reddy/F1itjeeMains2017.csv", "w")
for index in range(380):

    soup = BeautifulSoup(instant.present_html, "html.parser")

    s = soup.findAll("tbody")[2]


    for k in s.findAll("td"):

        sum = sum + 1
        if sum % 5 == 0:
            file.write(re.sub(r"( ){2,}"," ",k.getText().replace("\n"," ")).strip()+"\n")
        else:
            file.write(re.sub(r"( ){2,}"," ",k.getText().replace("\n"," ")).strip()+ ",")

    instant.next()

file.close()












