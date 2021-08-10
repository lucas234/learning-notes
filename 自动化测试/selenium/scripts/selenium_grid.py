# _*_ coding=utf-8 _*_
# class Singleton(object):
#     ''''' A python style singleton '''
#
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             print dir(cls)
#             org = super(Singleton, cls)
#             cls._instance = org.__new__(cls, *args, **kw)
#         print dir(cls)
#         return cls._instance
#
#
# if __name__ == '__main__':
#     class SingleSpam(Singleton):
#         def __init__(self, s):
#             self.s = s
#
#         def __str__(self):
#             return self.s
#
#
#     s1 = SingleSpam('spam')
#     print id(s1), s1
#     s2 = SingleSpam('spa')
#     print id(s2), s2
#     print id(s1), s1

# import selenium.webdriver.remote.webdriver
import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

# driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
# driver = selenium.webdriver.remote.webdriver.WebDriver(command_executor="http://127.0.0.1:4444/wd/hub",
#                                                        desired_capabilities=DesiredCapabilities.CHROME)
# 1.实现串行多浏览器执行脚本
# 浏览器数组
# lists = ['chrome', 'firefox']

# 通过不同的浏览器执行脚本
# for browser in lists:
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4444/wd/hub',
#         desired_capabilities={'platform': 'ANY',
#                               'browserName': browser,
#                               'version': '',
#                               'javascriptEnabled': True
#                               })
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys("python")
#     driver.find_element_by_id("su").click()
#     sleep(2)
# driver.quit()

# 2.实现串行多节点（分布式）执行脚本
d = {"http://192.168.40.220:5555/wd/hub": "chrome",
     "http://192.168.40.220:5556/wd/hub": "firefox"}
for host, browser in d.items():
    driver = webdriver.Remote(
        command_executor=host,
        desired_capabilities={'platform': 'ANY',
                              'browserName': browser,
                              'version': '',
                              'javascriptEnabled': True
                              })
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    driver.find_element_by_id("su").click()
    sleep(2)