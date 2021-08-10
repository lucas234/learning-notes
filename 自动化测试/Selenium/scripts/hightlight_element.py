# def fibonacci(n):
#     a, b, c = 0, 0, 1
#     while a < n:
#         b, c = c, c + b
#         yield b
#         a += 1
#
#
# print list(fibonacci(8))[-1]
#
# native, section, altered = [1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5], [4, 5, 5, "a"]
# add_list = []
# delete_list = []
# from collections import Counter
#
# items = Counter(altered)
# for i in items.keys():
#     if not section:
#         add_list = altered
#         break
#     if i in section:
#         if items.get(i) > 1:
#             for j in range(items.get(i) - 1):
#                 add_list.append(i)
#     else:
#         add_list.append(i)
#
# for k in section:
#     if k not in altered:
#         delete_list.append(k)
# print add_list
# print delete_list
# native = native + add_list
# [native.remove(i) for i in delete_list]
# print native

from selenium import webdriver


dr = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe")
dr.get("https://www.baidu.com/")

id_scripts = """document.getElementById("kw").style="border:2px solid red;";"""
css_scripts = """var elements = document.querySelector("#kw");
            if(elements){elements.style="border:2px solid red;";}"""
xpath_scriptes = """var elements = document.evaluate('//*[@id="kw"]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            elements.style="border:2px solid red;";"""
dr.execute_script(xpath_scriptes)
dr.find_element_by_id("kw").send_keys("selenium")

scripts_delete = """document.getElementsByName("wd")[0].style="border:none;";"""
dr.execute_script(scripts_delete)
scripts = """document.getElementById("su").setAttribute("style", "border:2px solid red;");"""
dr.execute_script(scripts)



# 获取元素中的文本内容
# 1、通过get_attribute(‘textContent’)(或者innerText、innerHTML属性都可以)来获取元素的文本值
# logoContext1 = driver.find_element_by_xpath('//div[@class="logo"]/span').get_attribute('textContent')

# 2、通过text来获取文本值(有时候通过.text获取不到,则可以用1的方法)
# logoContext2 = driver.find_element_by_xpath('//div[@class="logo"]/span').text

#3、通过执行JS操作来获取输入的文本值
# logoContext3 = "return document.getElementsByTagName('span')[0].innerText"
# driver.execute_script(logoContext3)


# scroll

# for i in range(100):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
