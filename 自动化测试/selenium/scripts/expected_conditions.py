# auther：Liul8
# date：2020/5/12 14:02
# tools：PyCharm
# Python：3.7.7
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# import time
#
# base_url = "https://www.baidu.com/"
# driver = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe")
# driver.get(base_url)
# # title_is 预期的title是否与当前网页的title一致，一致返回True，否则返回False
# print(ec.title_is("百度一下，你就知道")(driver))
# print(ec.title_is("百度一下，你也不知道")(driver))
# # title_contains 预期的title是否属于当前网页title的子串，是则返回True，否则返回False
# print(ec.title_contains("百度一下")(driver))
# print(ec.title_contains("百2一下")(driver))
#
# expect_url = "https://www.baidu.com/"
# expect_url2 = "https://test.com/"
# # url_changes 预期的URL是否与当前网页的URL一致，不一样则返回True，否则返回False
# print(ec.url_changes(expect_url)(driver))
# print(ec.url_changes(expect_url2)(driver))
# # url_contains 预期的URL是否是当前网页url子串，是则返回True，否则返回False
# print(ec.url_contains("baidu")(driver))
# # url_matches 与 url_contains类似，只是用的方法不一样，url_contains用的 sub-string in string, url_matches用的正则表达式
# print(ec.url_matches("baidu")(driver))
# # url_to_be 预期的URL与当前网页的URL是否一致，一致则返回True，否则返回False
# print(ec.url_to_be(expect_url)(driver))
# print(ec.url_to_be(expect_url2)(driver))
#
# print(ec.visibility_of(driver.find_element_by_id("kw")))
# print(ec.visibility_of_all_elements_located((By.ID, "kw"))(driver))
# print(ec.visibility_of_any_elements_located((By.ID, "kw"))(driver))
# print(ec.visibility_of_element_located((By.ID, "kw"))(driver))
# print(ec.invisibility_of_element_located((By.ID, "kw"))(driver))
# print(ec.invisibility_of_element((By.ID, "kw"))(driver))
#
# print(ec.text_to_be_present_in_element_value((By.ID, "kw"), "text_")(driver))
# print(ec.text_to_be_present_in_element((By.ID, "kw"), "text_")(driver))
#
# print(ec.staleness_of(driver.find_element_by_id("kw"))(driver))
# print(ec.presence_of_element_located((By.ID, "kw"))(driver))
# print(ec.presence_of_all_elements_located((By.ID, "kw"))(driver))
#
# print(ec.number_of_windows_to_be(5)(driver))
# print(ec.new_window_is_opened("current_window_handle")(driver))
#
# print(ec.frame_to_be_available_and_switch_to_it((By.ID, "kw"))(driver))
# print(ec.element_to_be_selected(driver.find_elements_by_id("kw"))(driver))
# print(ec.element_to_be_clickable((By.ID, "kw"))(driver))
# print(ec.element_selection_state_to_be(driver.find_elements_by_id("kw"), True)(driver))
# print(ec.element_located_to_be_selected((By.ID, "kw"))(driver))
# print(ec.element_located_selection_state_to_be((By.ID, "kw"), True)(driver))
# print(ec.alert_is_present()(driver))
#
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe"
base_url = r"C:\Users\liul8\Desktop\tips\test_local.html"

# chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
# base_url = r"C:\your path\test_local.html"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
driver.find_element_by_id("open_new_window").click()
result = wait.until(ec.number_of_windows_to_be(2))
print(result)
# 如果需要操作新Window的元素需要先切换
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element_by_id("kw")
try:
    result2 = wait.until(ec.number_of_windows_to_be(1))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.quit()
