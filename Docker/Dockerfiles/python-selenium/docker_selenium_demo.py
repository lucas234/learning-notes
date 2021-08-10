# @Time    : 2020/9/2 11:08
# @Author  : lucas
# @File    : docker_selenium_demo.py
# @Project : locust demo
# @Software: PyCharm

from selenium import webdriver
import time

desired_capabilities={
                      # 'platform':'ANY',
                      'browserName':'chrome',
                      # 'javascriptEnabled':True,
                      # 'marionette':False
                      }
remote_url = "http://chrome:4444/wd/hub"
driver = webdriver.Remote(remote_url,desired_capabilities=desired_capabilities)
driver.get('https://python.org')
print(driver.title)
print("begin ########")
print("begin ########")
print("begin ########")
print("begin ########")
print("begin ########")
print("begin ########")
print("begin ########")
driver.close()
time.sleep(10)