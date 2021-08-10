# auther：Liul8
# date：2020/5/21 17:11
# tools：PyCharm
# Python：3.7.7
# https://github.com/SergeyPirogov/webdriver_manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager(path=r"C:\diy\old coding\test\locust demo\Endtest\drivers",log_level=0).install())
print(ChromeDriverManager(log_level=0).install())
# driver.get("https://www.baidu.com/")
