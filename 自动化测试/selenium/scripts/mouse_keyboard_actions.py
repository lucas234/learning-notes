# auther：Liul8
# date：2020/5/21 10:37
# tools：PyCharm
# Python：3.7.7
# https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#module-selenium.webdriver.common.action_chains
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe"
base_url = "http://lucas234.gitee.io/static-demo/"
# r"file:///C:/Users/liul8/Desktop/tips/index.html"
# chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.baidu.com/")
# element = driver.find_element_by_id('alert')
actions = ActionChains(driver)
# # 鼠标左点击
# actions.click(element)
# # 鼠标左点击一直按着不放
# actions.click_and_hold(element)
# # 鼠标右击
# actions.context_click(element)
# # 双击
# actions.double_click(element)
# 拖拽
# driver.find_element_by_id('drag_and_drop').click()
# from_element = driver.find_element_by_id("square")
# to_element = driver.find_element_by_id("target")
# ActionChains(driver).pause(1).drag_and_drop(from_element, to_element).perform()

# # 新tab 页面打开链接, 另起一个窗口打开链接
# link = driver.find_element_by_id('drag_and_drop')
# actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
# # on mac
# actions.key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
# actions.key_down(Keys.SHIFT).click(link).key_up(Keys.SHIFT).perform()


# # 全选复制,全选，复制
# actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# # 悬浮显示子菜单,选择子菜单
# driver.find_element_by_id("dropdownlist").click()
# menu_element = driver.find_element_by_class_name('dropbtn')
# sub_element = driver.find_element_by_xpath('//a[text()="Link 2"]')
# actions.move_to_element(menu_element).click(sub_element).perform()


# 键盘输入操作

# 输入框输入内容
driver.find_element_by_id("kw").send_keys("验证删除多的字字")
time.sleep(2)
# 删除一个字符
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# 输入空格键 + 字符
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("appium")
time.sleep(2)

# ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys("全选的内容")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(2)

# ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(2)

# ctrl+v 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 点击回车键
driver.find_element_by_id("su").send_keys(Keys.ENTER)

