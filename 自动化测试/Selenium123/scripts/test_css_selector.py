# auther：Liul8
# date：2020/5/9 9:40
# tools：PyCharm
# Python：3.7.7

from selenium import webdriver


dr = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe")
dr.get(r"file:///C:/Users/liul8/Desktop/test_css_selector.html")
dr.find_element_by_css_selector("input#Email").send_keys("test ID selector")
# dr.find_element_by_css_selector("#Email").send_keys("test ID selector")
# dr.find_element_by_css_selector("input.password").send_keys("test class selector")
dr.find_element_by_css_selector(".password").send_keys("test class selector")
# dr.find_element_by_css_selector("input[type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input[id='Test_attribute'][type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input#Test_attribute[type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input.inputtext[type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input[id^='Test_I']").send_keys("test sub-string selector")
# dr.find_element_by_css_selector("input[id$='001']").send_keys("test sub-string selector")
# dr.find_element_by_css_selector("input[id*='ID']").send_keys("test sub-string selector")
print(dr.find_element_by_css_selector("div[id~='c2']").text)
print(dr.find_element_by_css_selector("div[class|='five']").text)
# 选择id值包含Test且不包含attribute的属性
# dr.find_element_by_css_selector("input[id*='Test']:not([id*='attribute'])").send_keys("test sub-string selector")
# 定位子元素
dr.find_element_by_css_selector("div#buttonDiv input").send_keys("test child element")
# 定位多个子元素
print(dr.find_element_by_css_selector("ul#automation li:first-child").text)
print(dr.find_element_by_css_selector("ul#automation li:last-child").text)
print(dr.find_element_by_css_selector("ul#automation li:nth-of-type(2)").text)

# print(dr.find_element_by_css_selector("button:contains('test1_button')").get_attribute('id'))
print(dr.find_element_by_css_selector("button#test-button span").text)
print(dr.find_element_by_css_selector("[id='two']").text)
print(dr.find_element_by_css_selector("[id^='tw']").text)
