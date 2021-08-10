# @Time    : 2020/8/14 9:22
# @Author  : lucas
# @File    : full_screenshot.py
# @Project : locust demo
# @Software: PyCharm
# https://stackoverflow.com/questions/41721734/take-screenshot-of-full-page-with-selenium-python-with-chromedriver

from selenium import webdriver
import time

url = "https://www.baidu.com/s?wd=test&rsv_spt=1&rsv_iqid=0xdd61b9640000a9fe&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1000&rsv_sug4=1735"

# # # firefox 浏览器
# firefox_path = r"C:\Users\liul8\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=firefox_path)
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
# ele = driver.find_element_by_tag_name("body")
# print(ele.size)
# driver.set_window_size(ele.size["width"], ele.size["height"])
# time.sleep(1)
# driver.save_screenshot("test12345.png")
# driver.close()

# # chrome 必须再无头条件下才可以截取全屏
# chrome_path = r"C:\Users\liul8\Downloads\chromedriver_win32\chromedriver.exe"
# chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--start-maximized')

# driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
# driver.get(url)
# time.sleep(3)
# ele = driver.find_element_by_tag_name("body")
# print(ele.size)
# driver.set_window_size(ele.size["width"], ele.size["height"])
# time.sleep(1)
# driver.save_screenshot("test12345.png")
# driver.close()


# 利用js
chrome_path = r"C:\Users\liul8\Downloads\chromedriver_win32\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# chrome_options.headless = True
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
driver.get(url)
time.sleep(3)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
driver.quit()

# # js 获取body的长、宽
# width = driver.execute_script('return document.body.parentNode.scrollWidth')
# height = driver.execute_script('return document.body.parentNode.scrollHeight')
# print(height, width)
