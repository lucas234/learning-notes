# auther：Liul8
# date：2020/5/21 16:14
# tools：PyCharm
# Python：3.7.7
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.select.html#module-selenium.webdriver.support.select
from selenium import webdriver
from selenium.webdriver.support.select import Select


chrome_driver_path = r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe"
base_url = "http://lucas234.gitee.io/static-demo/"
# chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
driver.find_element_by_id('dropdownlist').click()
selects = driver.find_element_by_id('cars')

# 通过索引选择
Select(selects).select_by_index(0)
# 通过值选择
Select(selects).select_by_value('audi')
# 通过显示的文本
Select(selects).select_by_visible_text('Saab')

# 打印所有的值
print([opt.get_attribute("value") for opt in Select(selects).options])


