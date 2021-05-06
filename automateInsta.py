'''
  This is the python implementation for the InstaBOt Part 2 Project .
  
  Author : Vamsi Krishna Katam
'''


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

class AutomateInsta:
    def __init__(self,driver):
        self.driver = driver 

    def open(self,url):
        self.driver.get(url)
        time.sleep(4)
    

    def login(self,user_name,password):
    
        #username
        self.driver.find_element_by_name('username').send_keys(user_name)
        #password
        self.driver.find_element_by_name('password').send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//div[contains(@class,"DhRcB")]/button')
        login_btn.submit()

        time.sleep(5)

        save_not_now_btn = self.driver.find_element_by_xpath('//div[contains(@class,"cmbtv")]/button')
        save_not_now_btn.click()
        
        time.sleep(5)
        not_pop_up_win = self.driver.find_elements_by_xpath('//div[contains(@class,"mt3GC")]/button')
        not_pop_up_win[1].click()  # clicking not now 
        print('Successfully Logged in')

    
    def logout(self,user_name):
        url = 'https://www.instagram.com/{0}/'.format(user_name)
        self.driver.get(url)
        wait = WebDriverWait(self.driver,5)
        wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class = 'Fifk5']")))
        self.driver.find_element_by_xpath("//div[@class = 'Fifk5']/span").click()
        time.sleep(2)
        self.driver.find_elements_by_xpath('//div[contains(@class,"-qQT3")]')[1].click()
        print('Succeffully Logged Out')

    
    def get_insta_handles(self,keyword):
        search_input = self.driver.find_element_by_xpath('//div[contains(@class,"LWmhU")]/input')
        search_input.clear()
        time.sleep(2)
        search_input.send_keys(keyword)

        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_element_located((By.XPATH,'//a[@class = "-qQT3"]')))

        handles_class = self.driver.find_elements_by_xpath('//a[@class = "-qQT3"]')
        
        handles = []
        try:
            for i in handles_class:
                soup = BeautifulSoup(i.get_attribute('outerHTML'),'html.parser')
                handle = soup.find(class_ = "_7UhW9").text
                if handle[0] == '#':
                    handle = handle[1:]
                handles.append(handle)
        except StaleElementReferenceException:
            print('Please check your keyword')
            
        return handles

    def get_followers_count(self,handle):
        url = 'https://www.instagram.com/{0}/'.format(handle)
        self.driver.get(url)
        time.sleep(3)
        count = self.driver.find_elements_by_class_name('g47SY ')[1].get_attribute('title')
        count = int(count.replace(',',""))
        return count



        

    
        