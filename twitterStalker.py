# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 17:10:40 2023
"""

# Import Dependencies

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = ""
doc_PATH = ""

driver = webdriver.Chrome(PATH)
driver.get("https://twitter.com/login")

subject = ""
username= ""
password= ""


# Setup the log in
sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")
username.send_keys(username)
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Siguiente')]")
next_button.click()

sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")
password.send_keys(password)
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Iniciar sesión')]")
log_in.click()

# Search item and fetch it
sleep(3)
search_box = driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
search_box.send_keys(subject)
search_box.send_keys(Keys.ENTER)

sleep(3)
people = driver.find_element(By.XPATH,"//span[contains(text(),'People')]")
people.click()

sleep(3)
profile = driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]")
profile.click()



# UserTag = driver.find_element(By.XPATH,"//div[@data-testid='User-Names']").text
# TimeStamp = driver.find_element(By.XPATH,"//time").get_attribute('datetime')
# Tweet = driver.find_element(By.XPATH,"//div[@data-testid='tweetText']").text
# Reply = driver.find_element(By.XPATH,"//div[@data-testid='reply']").text
# reTweet = driver.find_element(By.XPATH,"//div[@data-testid='retweet']").text
# Like = driver.find_element(By.XPATH,"//div[@data-testid='like']").text


UserTags=[]
TimeStamps=[]
Tweets=[]
Replys=[]
reTweets=[]
Likes=[]

articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
while True:
    for article in articles:
        UserTag = driver.find_element(By.XPATH,".//div[@data-testid='User-Name']").text
        UserTags.append(UserTag)
        
        TimeStamp = driver.find_element(By.XPATH,".//time").get_attribute('datetime')
        TimeStamps.append(TimeStamp)
        
        Tweet = driver.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        Tweets.append(Tweet)
        
        Reply = driver.find_element(By.XPATH,".//div[@data-testid='reply']").text
        Replys.append(Reply)
        
        reTweet = driver.find_element(By.XPATH,".//div[@data-testid='retweet']").text
        reTweets.append(reTweet)
        
        Like = driver.find_element(By.XPATH,".//div[@data-testid='like']").text
        Likes.append(Like)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(3)
    articles = driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    Tweets2 = list(set(Tweets))
    if len(Tweets2) > 5:
        break


print(len(UserTags),
len(TimeStamps),
len(Tweets),
len(Replys),
len(reTweets),
len(Likes))


import pandas as pd

df = pd.DataFrame(zip(UserTags,TimeStamps,Tweets,Replys,reTweets,Likes)
                  ,columns=['UserTags','TimeStamps','Tweets','Replys','reTweets','Likes'])

df.head()
###DOCPATH
##df.to_excel(r"",index=False)


###DOCPATH with \\
import os
os.system(r'start "excel" ""')