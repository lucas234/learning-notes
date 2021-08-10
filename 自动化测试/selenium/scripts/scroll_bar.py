# _*_ coding=utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.find_element_by_id('kw').send_keys('sikuli')
driver.find_element_by_id('su').click()
time.sleep(5)
# first method
# js = "window.scrollTo(0,document.body.scrollHeight)"
# driver.execute_script(js)
# time.sleep(3)
# js = "window.scrollTo(0,0)"
# driver.execute_script(js)

# second
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)
# time.sleep(3)
# js = "var q=document.documentElement.scrollTop=0"
# driver.execute_script(js)

# third 滚动条拉到指定位置（具体元素）
# target = driver.find_element_by_id("rs")
# driver.execute_script("arguments[0].scrollIntoView();", target)


# fourth 类似于按键盘上的PgDn按键，可以换成Keys.DOWN(下箭头，不过这个下拉进度比较慢)
for i in range(6):
    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
    time.sleep(1)

time.sleep(3)
driver.close()