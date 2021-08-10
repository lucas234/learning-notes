

### 显式等待

`WebDriver` 显式等待，除非在规定时间内满足指定的条件，否则一直等待直到抛出超时异常`TimeoutException` 。默认 0.5s 调用`ExpectedCondition` 一次，直到返回值或者抛出异常。

##### 入参介绍

- **driver** – WebDriver 实例 (Ie, Firefox, Chrome, Remote 等); mandatory argument
- **timeout** – 等待时间
- **poll_frequency** – 轮询间隔. 默认0.5s
- **ignored_exceptions** – 运行期间忽略的异常; 默认只忽略`NoSuchElementException`

```python
wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=(NoSuchElementException,))
```

### ExpectedConditions  样例

#### 1. alert_is_present

判断页面上是否存在alert

**Parameters**：没有参数

**Returns:**

如果存在则返回alert对象，不存在则抛出`selenium.common.exceptions.TimeoutException`异常

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
driver.find_element_by_id("alert").click()
wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print alert.text
alert.accept()
driver.close()
```



#### 2. element_located_selection_state_to_be(locator, is_selected)

判断元素显示在页面上并且选中状态是否符合预期

**Parameters**：

locator – 一个元组 (By.XX, value)，(By.ID, "password")等

is_selected – 传入一个bool值； True – 元素应该处于被选中状态.；False – 元素应该处于非选中状态。

**Returns:**

如果element 在最大等待时间内被找到并且处于期望的状态则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)

result = wait.until(ec.element_located_selection_state_to_be((By.ID, 'savingsaccount'), True))
# change True to False to see TimeoutException
print(result)

result = wait.until(ec.element_located_selection_state_to_be((By.ID, 'currentaccount'), False))
# change False to True to see TimeoutException
print(result)
driver.close()
```

#### 3. element_located_to_be_selected(locator)

判断元素显示在页面上并且处于选中状态

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
element 被找到并且处于选中状态返回 True；否则抛出`selenium.common.exceptions.TimeoutException`异常

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.element_located_to_be_selected((By.ID, 'savingsaccount')))
print(result)
driver.close()
```



#### **4. element_selection_state_to_be(element, is_selected)**

与`element_located_selection_state_to_be` [( #2 )](2. element_located_selection_state_to_be(locator, is_selected)) 一致，只是传参不一样，此处直接传入 `web element`而不是 `locator`.

**Parameters:**
element – web element，例如：element = driver.find_elements_by_id("")，传入element 
is_selected – 传入一个bool值； True – 元素应该处于被选中状态.；False – 元素应该处于非选中状态。

**Returns:**
如果element 在最大等待时间内被找到并且处于期望的状态则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)

result = wait.until(ec.element_selection_state_to_be(driver.find_element_by_id("savingsaccount"), True))
# change True to False to see TimeoutException
print(result)
result = wait.until(ec.element_selection_state_to_be(driver.find_element_by_id("currentaccount"), False))
# change False to True to see TimeoutException
print(result)
driver.close()
```



#### **5. element_to_be_clickable(locator)**

判断某个元素中是否可见并且是enable的

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
element – 如果该元素是可点击的则返回该元素，否则否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)
element = wait.until(ec.element_to_be_clickable((By.ID, 'alert')))
element.click()
time.sleep(3)
driver.close()
```



#### 6. element_to_be_selected(element)

与`element_located_to_be_selected` （[#3](3. element_located_to_be_selected(locator))）一致，只是传参不一样，此处直接传入 `web element`而不是 `locator`.

**Parameters:**
element – web element，例如：element = driver.find_elements_by_id("")，传入element

**Returns:**
元素被选中则返回True，否则否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)
subscribe_checkbox = driver.find_element_by_id('savingsaccount')
result = wait.until(ec.element_to_be_selected(subscribe_checkbox))
print(result)
driver.close()
```

#### 7. frame_to_be_available_and_switch_to_it(locator)

等待frame可用并且跳转进frame（可操作frame中的元素）. 

**Parameters:**

locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
frame可用并且跳转进frame则返回True，否则否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
start = time.time()
driver.get("http://lucas234.gitee.io/static-demo/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.frame_to_be_available_and_switch_to_it((By.ID, "iframes")))
print(result)
driver.find_element_by_id("test_iframe").click()
driver.close()
```

#### 8. invisibility_of_element(locator)

等待元素不可见或被移除. 

**Parameters:**

locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
在web页面，如果元素上被移除则返回True；由可见变为隐藏则返回该元素本身，否则否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
driver.find_element_by_id("invisibility_element").click()
wait = WebDriverWait(driver, 5)
# 如果元素是隐藏，则返回元素本身，text_id_1设置1s后隐藏
result = wait.until(ec.invisibility_of_element((By.ID, "text_id_1")))
print(result.get_attribute("textContent"))
# 如果是删掉，则返回 True， text_id_1设置3s后删除
result1 = wait.until(ec.invisibility_of_element((By.ID, "text_id_2")))
print(result1)
# 如果元素一直存在则抛出TimeoutException
try:
    result2 = wait.until(ec.invisibility_of_element((By.ID, "text_id_3")))
    print(result2)
except TimeoutException:
    print("超时异常！")
driver.close()
```

#### 9. invisibility_of_element_located(locator)

等待元素不可见或被移除. 与`invisibility_of_element` （[#8](8. invisibility_of_element(locator))）一致，传参也一致

**Parameters:**

locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
在web页面，如果元素上被移除则返回True；由可见变为隐藏则返回该元素本身，否则否则抛出`selenium.common.exceptions.TimeoutException`异常。

#### 10. title_is(title)

检查title是否与预期严格一致，字母大小写敏感.

**Parameters:**

title – 字符串，预期的 title

**Returns:**

如果与预期的一致则返回 True，否则抛出`selenium.common.exceptions.TimeoutException`异常。
**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
print(driver.title)
# 返回 True
result = wait.until(ec.title_is("selenium tips"))
print(result)
# 抛出异常
try:
    result1 = wait.until(ec.title_is("selenium tips111"))
    print(result1)
except TimeoutException:
    print("超时异常！")
driver.close()
```



#### 11. title_contains(title)

检查title是否包含预期字符，字母大小写敏感.

**Parameters:**

title – 字符串，预期的 title

**Returns:**

如果包含预期的字符则返回 True，否则抛出`selenium.common.exceptions.TimeoutException`异常。
**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
print(driver.title)
# 返回 True
result = wait.until(ec.title_contains("tips"))
print(result)
# 抛出异常
try:
    result1 = wait.until(ec.title_contains("selenium111"))
    print(result1)
except TimeoutException:
    print("超时异常！")
driver.close()
```

#### 12. presence_of_all_elements_located(locator)

判断所有元素是否存在在 web 页面上，类似于多个元素拥有同一个ID 

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
如果匹配到，则返回一个包含所有配到的元素的列表 list.否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
# 返回所有元素列表
results = wait.until(ec.presence_of_all_elements_located((By.ID, "alert")))
print(results)
for element in results:
    print(element.get_attribute("id"))
# 抛出异常
try:
    result1 = wait.until(ec.presence_of_all_elements_located((By.ID, "alert11")))
    print(result1)
except TimeoutException:
    print("超时异常！")
driver.close()
```

#### 13. presence_of_element_located(locator)

判断元素是否存在在 web 页面上，不管元素是否可见（即如果元素是隐藏的，也算存在在页面上） 

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
如果存在，返回查找到的元素.否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
# 返回元素
result = wait.until(ec.presence_of_element_located((By.ID, "no-display")))
print(result.get_attribute("textContent"))
driver.close()
```

#### 14. visibility_of(element)

判断元素是否可见，可见 意味着不仅存在（即元素的 display 属性为非 none），而且意味着该元素的长宽大于0

**Parameters:**
element -- web element，例如：element = driver.find_elements_by_id("")，传入element

**Returns:**
如果可见，返回查找到的元素.否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
# 可见元素
element = driver.find_element_by_id("alert")
result = wait.until(ec.visibility_of(element))
print(result.get_attribute("textContent"))
# 存在不可见元素
try:
    element1 = driver.find_element_by_id("no-display")
    result1 = wait.until(ec.visibility_of(element1))
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 15. visibility_of_element_located(locator)

与 `visibility_of`（[#14][14. visibility_of(element)]）用法一致，只是传参不一样，传入 locator 而不是 element 

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
如果可见，返回查找到的元素.否则抛出`selenium.common.exceptions.TimeoutException`异常。

#### 16. visibility_of_all_elements_located(locator)

判断查找到的所有元素是否可见。例如，通过该 locator 定位到了6个元素，但是只有4 个可见，其他2个隐藏，则必须等待6个元素都显式可见。

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
如果所有元素可见，则返回一个包含所有元素的列表 list，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
driver.find_element_by_id("visibility_element").click()
# 此时可以打印出 7 ，如果将上边的的等待时间改成7 则抛出异常
results = wait.until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "display")))
print(len(results))
print(results[0].text)
driver.close()
```

#### 17. visibility_of_any_elements_located(locator)

判断查找到的所有元素中至少一个是否可见。例如，通过该 locator 定位到了6个元素，只要有一个元素可见即满足条件。

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等

**Returns:**
如果查找到的所有元素中至少一个可见，则返回一个包含所有*可见*元素的列表 list（如果找到7个元素，6个可见，1个隐藏，则返回包含6个元素的列表），否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
driver.find_element_by_id("visibility_element").click()
# 此时可以打印出 6
results = wait.until(ec.visibility_of_any_elements_located((By.CLASS_NAME, "display")))
print(len(results))
print(results[0].text)
driver.close()
```

#### 18. text_to_be_present_in_element(locator, text)

判断查找到的元素的text是否包含预期的字符串

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等
text –  预期字符串

**Returns:**
如果包含则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
result = wait.until(ec.text_to_be_present_in_element((By.ID, "invisibility_element"), "invisibility element"))
print(result)
result1 = wait.until(ec.text_to_be_present_in_element((By.ID, "invisibility_element"), "invisibility"))
print(result1)

try:
    result2 = wait.until(ec.text_to_be_present_in_element((By.ID, "invisibility_element"), "invisibility11"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 19. text_to_be_present_in_element_value(locator, text)

判断查找到的元素的属性value的值是否包含预期的字符串

**Parameters:**
locator – 一个元组 (By.XX, value)，(By.ID, "password")等
text –  预期字符串

**Returns:**
如果包含则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
result = wait.until(ec.text_to_be_present_in_element_value((By.ID, "sub-cars"), "fiat"))
print(result)
result1 = wait.until(ec.text_to_be_present_in_element_value((By.ID, "sub-cars"), "fi"))
print(result1)

try:
    result2 = wait.until(ec.text_to_be_present_in_element_value((By.ID, "sub-cars"), "invisibility11"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 20. url_changes(url)

判断当前网页url是否与预期的不一致. 

**Parameters:**
url – 期望的url

**Returns:**
预期URL与当前URL不一致则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.baidu.com/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.url_changes("https://www.google.com/"))
print(result)

try:
    result2 = wait.until(ec.url_changes("https://www.baidu.com/"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 21. url_contains(url)

判断当前网页的url是否包含预期的子串. 

**Parameters:**
url – 预期的url子串

**Returns:**
如果包含预期URL的子串则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.baidu.com/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.url_contains("baidu"))
print(result)
try:
    result2 = wait.until(ec.url_contains("google"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 22. url_matches(pattern)

判断当前网页的 url 是否满足匹配 pattern，pattern是一个正则表达式

**Parameters:**
url – 正则表达式，必须完全匹配

**Returns:**
如果匹配正则表达式则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.baidu.com/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.url_matches("https:*"))
print(result)
try:
    result2 = wait.until(ec.url_matches("https://*google*"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 23. url_to_be(url)

判断当前网页的URL是否与预期的URL一致. 

**Parameters:**
url – 预期的URL

**Returns:**
如果与预期的URL一致则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.baidu.com/")
wait = WebDriverWait(driver, 5)
result = wait.until(ec.url_to_be("https://www.baidu.com/"))
print(result)
try:
    result2 = wait.until(ec.url_to_be("https://www.google.com/"))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 24. staleness_of(element)

判断元素不再存在在web页面上，适用于元素在当前页面被删除或者判断进入到新的界面等. 

**Parameters:**
element-- web element，例如：element = driver.find_elements_by_id("")，传入element

**Returns:**
如果元素不可用或者不存在（隐藏的元素看做存在）则返回True，否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
driver.find_element_by_id("invisibility_element").click()
element = driver.find_element_by_id("text_id_2")
element1 = driver.find_element_by_id("text_id_1")
result = wait.until(ec.staleness_of(element))
print(result)
try:
    result2 = wait.until(ec.staleness_of(element1))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.close()
```

#### 25. new_window_is_opened(current_handles)

判断是否新打开了一个网页句柄且网页句柄数量增加.

**Parameters:**
current_handles – driver.window_handles

**Returns:**
如果打开了新的网页句柄并且数量增加则返回True， 否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
wait = WebDriverWait(driver, 5)
window_nums1 = driver.window_handles
print(window_nums1)
driver.find_element_by_id("open_new_window").click()
result = wait.until(ec.new_window_is_opened(window_nums1))
print(result)
# 如果需要操作新Window的元素需要先切换
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element_by_id("kw")
try:
    window_nums2 = driver.window_handles
    result2 = wait.until(ec.new_window_is_opened(window_nums2))
    print(result2)
except TimeoutException as e:
    print("超时异常！")
driver.quit()
```

#### 26. number_of_windows_to_be(num_windows)

判断当前所有的网页句柄数量是否等于某一个确定的值.

**Parameters:**
num_windows– 具体整形数字

**Returns:**
如果当前所有的网页句柄数量等于某一个确定的值则返回True， 否则抛出`selenium.common.exceptions.TimeoutException`异常。

**Example:**

```python
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
base_url = r"http://lucas234.gitee.io/static-demo/"
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

```

至此，所有显式等待已经介绍完毕。

### 参考

[https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html](https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html)

[https://pypi.org/project/selenium/](https://pypi.org/project/selenium/)

[https://www.selenium.dev/selenium/docs/api/py/api.html](https://www.selenium.dev/selenium/docs/api/py/api.html)

[https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol](https://github.com/SeleniumHQ/selenium/wiki/JsonWireProtocol)

