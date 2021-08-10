# _*_ coding=utf-8 _*_
from selenium import webdriver
import os
import time

url = "http://www.sahitest.com/demo/php/fileUpload.htm"
driver = webdriver.Chrome()
driver.get(url)
# first
# driver.find_element_by_xpath('//*[@id="file4"]').send_keys("C:\\Users\\saas\\Desktop\\ump.xlsx")

# second
driver.find_element_by_xpath('//*[@id="file"]').click()
command = "C:\\Users\\saas\\Desktop\\upload.exe" + " " + "chrome" + " " + "C:\\Users\\saas\\Desktop\\ump.xlsx"
os.system(command)
time.sleep(3)
driver.close()
