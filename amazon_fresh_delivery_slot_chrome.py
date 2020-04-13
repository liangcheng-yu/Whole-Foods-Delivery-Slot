import bs4

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import sys
import time
import os
import random

WARNING_UP_S = 120
REFRESH_PERIOD_S_MIN = 10
REFRESH_PERIOD_S_MAX = 15

DRIVER_PATH = "/Users/liangchengyu/Downloads/chromedriver"

def getWFSlot(productUrl):
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
   }

   driver = webdriver.Chrome(executable_path=DRIVER_PATH)
   driver.get(productUrl)           
   html = driver.page_source
   soup = bs4.BeautifulSoup(html, features="html.parser")
   print("120s to enter the right page...")
   time.sleep(WARNING_UP_S)
   no_open_slots = True

   while no_open_slots:
      driver.refresh()
      print("=============================")
      print("page refreshed")
      html = driver.page_source
      soup = bs4.BeautifulSoup(html, features="html.parser")

      slot_not_available_text = "Not available"
      all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
      try:
         for each_date in all_dates:
            if slot_not_available_text not in each_date.text:
               print('Slot open for the date block')
               os.system('say "Slots for delivery opened!"')
               time.sleep(random.randint(REFRESH_PERIOD_S_MIN,REFRESH_PERIOD_S_MAX))   
      except AttributeError:
         pass
      
      wait_time = random.randint(REFRESH_PERIOD_S_MIN,REFRESH_PERIOD_S_MAX)
      print("wait for "+wait_time+"s before next refresh")
      time.sleep(wait_time)


getWFSlot('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')


