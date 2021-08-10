# auther：Liul8
# date：2020/4/20 10:46
# tools：PyCharm
# Python：3.7.7
from selenium import webdriver


# If your website has SSL errors, ignoring certificate errors
# chrome_options.add_argument('--ignore-certificate-errors')

# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors.
driver = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe",
                          chrome_options=chrome_options,
                          service_args=['--verbose', r'--log-path=C:\diy\old coding\test\locust demo\chromedriver.log'])

# # Option 2 - with pyvirtualdisplay run on linux,reference:https://blog.testproject.io/2018/02/20/chrome-headless-selenium-python-linux-servers/
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(1024, 768))
# display.start()
# driver = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe",
#   service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])

# Log path added via service_args to see errors if something goes wrong (always a good idea - many of the errors I encountered were described in the logs)

# And now you can add your website / app testing functionality:
driver.get('https://python.org')
print(driver.execute_script("return document.readyState"))  # 只适用于页面全部加载，不适用于部分加载（识别不到）
import time
# time.sleep(20)
# 判断 jQuery 是否被定义
print(driver.execute_script("return !!window.jQuery"))
# 判断是否有jQuery及加载完成
print(driver.execute_script("return !!window.jQuery && window.jQuery.active == 0"))
driver.save_screenshot('test.png')
print(driver.title)
