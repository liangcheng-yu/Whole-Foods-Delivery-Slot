import bs4

from selenium import webdriver

import sys
import time
import os

import random

DRIVER_PATH = "/Users/liangchengyu/Downloads/chromedriver"
REFRESH_PERIOD_S_MIN = 10
REFRESH_PERIOD_S_MAX = 15


def getWFSlot(productUrl):
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
   }

   driver = webdriver.Chrome(executable_path=DRIVER_PATH)
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html, "html.parser")
   time.sleep(180)
   no_open_slots = True

   while no_open_slots:
      driver.refresh()
      print("refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html, "html.parser")
      time.sleep(random.randint(REFRESH_PERIOD_S_MIN,REFRESH_PERIOD_S_MAX)) 

      try:
         slot_not_available_text = "Not available"
         all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
         for each_date in all_dates:
            if slot_not_available_text not in each_date.text:
               print('SLOTS OPEN 2!')
               os.system('say "Slots for delivery opened!"')
               time.sleep(60)
      except AttributeError:
         pass

      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
            print("NO SLOTS!")
      except AttributeError: 
            print('SLOTS OPEN 3!')
            os.system('say "Slots for delivery opened!"')
            time.sleep(60)


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


