# import libraries 

from bs4 import BeautifulSoup
import requests
from requests.auth import AuthBase

import time
import datetime


import smtplib
# Connect to Website and pull in data

URL = 'https://www.amazon.com/Amazon-Essentials-Classic-Fit-Short-Khaki/dp/B01JQTN8SQ/ref=d_slmt_fabric_cml_detail_d_sccl_1_5/146-1661313-3205754?pd_rd_w=5AZPZ&content-id=amzn1.sym.b445bfb9-712c-45d1-a72a-63721cb24e3c&pf_rd_p=b445bfb9-712c-45d1-a72a-63721cb24e3c&pf_rd_r=R8AZVQZ16FY9SRZ8SFPV&pd_rd_wg=ZxvlP&pd_rd_r=ae9d4bfa-56ec-4514-8a57-8b8b8c45529c&pd_rd_i=B01JQTN8SQ&psc=1'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "lxml")

soup2 = BeautifulSoup(soup1.prettify(), "lxml")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(class_='a-offscreen').get_text()

print(title)
print(price)
                
# Clean up the data a little bit

price = price.strip()[1:]
title = title.strip()

print(title)
print(price)

# Create a Timestamp for your output to track when data was collected

import datetime

today = datetime.date.today()

print(today)

# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]


with open('AmazonWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)

import pandas as pd

df = pd.read_csv(r'C:\Users\Lenovo\AmazonWebScraperDataset.csv')

print(df)

#Now we are appending data to the csv

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
#Combine all of the above code into one function


def check_price():
    URL = 'https://www.amazon.com/Amazon-Essentials-Classic-Fit-Short-Khaki/dp/B01JQTN8SQ/ref=d_slmt_fabric_cml_detail_d_sccl_1_5/146-1661313-3205754?pd_rd_w=5AZPZ&content-id=amzn1.sym.b445bfb9-712c-45d1-a72a-63721cb24e3c&pf_rd_p=b445bfb9-712c-45d1-a72a-63721cb24e3c&pf_rd_r=R8AZVQZ16FY9SRZ8SFPV&pd_rd_wg=ZxvlP&pd_rd_r=ae9d4bfa-56ec-4514-8a57-8b8b8c45529c&pd_rd_i=B01JQTN8SQ&psc=1'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "lxml")

    soup2 = BeautifulSoup(soup1.prettify(), "lxml")

    title = soup2.find(id='productTitle').get_text()

    price = soup2.find(class_='a-offscreen').get_text()
    
    price = price.strip()[1:]
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv 
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]


    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(5)

import pandas as pd

df = pd.read_csv(r'C:\Users\lenovo\AmazonWebScraperDataset.csv')

print(df)


