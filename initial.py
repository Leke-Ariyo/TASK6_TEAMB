from selenium import webdriver
import pandas as pd
import requests
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
from selenium.common.exceptions import NoSuchElementException

class Account_Scraper():
    def __init__(self,email,password):
        self.email = email
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(executable_path ='chromedriver.exe',chrome_options=options)
        
    def signIn(self):
        self.driver.get('https://web.facebook.com/login')
        self.a = self.driver.find_element_by_id('email')
        self.a.send_keys(self.email)
        print ("Email Id entered...")
        self.b = self.driver.find_element_by_id('pass')
        self.b.send_keys(self.password)
        print ("Password entered...")
        self.c = self.driver.find_element_by_id('loginbutton')
        self.c.click()

        #send message
        #person_to_message = input("Enter user ID of person to message")
        #person_to_message_url = "https://web.facebook.com/"+person_to_message
        #time.sleep(5)
        #get to messenger
        #self.driver.get(person_to_message_url)

        #self.driver.find_element_by_css_selector("._1mf _1mj").send_keys("Merhaba, nasilsiniz?")
        #self.fetch_place = self.driver.find_element_by_xpath("//*[@class='_1p1t']").send_keys("Merhaba, nasilsiniz?") _5rpb
        #self.fetch_place = self.driver.find_element_by_xpath("//*[@class='_1p1v']").send_keys("Merhaba, nasilsiniz?")
        """
        try:
            self.driver.get("https://web.facebook.com/messages/t/ariyoleke")
            #self.driver.switch_to_active_element().send_keys("HI, \n its a test message \n plz don't reply \n")
            time.sleep(1)
        except UnexpectedAlertPresentException:
            self.driver.switch_to_alert().accept()  
        except Exception:
            pass
            #continue
        """
        #group invite
        """self.driver.get("https://www.facebook.com/groups/522229201193013/") 
        invitation_box = self.driver.find_element_by_xpath("//*[@class='inputtext textInput']")
        invitation_box.send_keys("Abdulwahab Abdulrasaq")
        invitation_box.send_keys(Keys.ENTER)"""

        #add_a_comment
        """
        self.driver.get("https://m.facebook.com/ariyoleke/posts/1512693518802189") 
        #comment_box = self.driver.find_element_by_css_selector('body[dir=ltr]')
        #comment_box = self.driver.find_element_by_xpath("//*[@class='_3og5 _5wel hasLeftCol _2yq home composerExpanded _5vb_ fbx _-kb _61s0 _605a v_1g8w-hy8pe chrome webkit win x1 Locale_en_US cores-gte4 _19_u hasAXNavMenubar']")
        #comment_box = self.driver.find_element_by_xpath("//*[@class=' _129h']")
        comment_box=self.driver.find_element_by_id("composerInput")
        #time.sleep(5)
        #comment_box.click()
        #time.sleep(5)
        comment_box.send_keys("HI")
        post_comment = self.driver.find_element_by_tag_name('button')
        time.sleep(5)
        post_comment.click()
        print("Commented posted successfully")"""

        #send_friend_requests
        self.driver.get("https://www.facebook.com")
        try:
            self.driver.find_element_by_id('u_0_e').click()
        except NoSuchElementException: 
            print("Your username and/or password appear to be incorrect")
        try:
            self.driver.find_element_by_partial_link_text('Add Friend').click()
            self.driver.get("https://www.facebook.com") 

        except NoSuchElementException:
            pass



        


email = "lexmill99@gmail.com", 
password = "lekeariyo2015", 
facebook = Account_Scraper(email,password)
facebook.signIn()
