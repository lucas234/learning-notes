## `一、ActionChains` 进行鼠标操作 

在自动化的过程中，常常会遇到一些鼠标操作，常见的一些场景如下：

- 鼠标悬浮到菜单栏显示子菜单栏
- 鼠标右键元素执行一些操作
- 鼠标拖拽操作
- 双击
- 其他

### What  is `ActionChains`?

`ActionChains`是一种自动化低级交互的方法，例如鼠标移动、鼠标按钮操作、按键和上下文菜单交互。对于执行更复杂的操作(比如悬停和拖放)非常有用。

当你在`ActionChains`对象上调用方法操作的对象时，这些操作被存储在`ActionChains`对象的一个队列中。当您调用`perform()`时，事件按它们排队的顺序被触发。

###### `ActionChains` 链模式使用，所有方法在一行:

```python
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
```

###### 或者`ActionChains` 排队模式使用，一个一个排队，然后执行:

```python
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_css_selector(".nav")
hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")
actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
```



### 所有 `ActionChains` 可调用的方法

#### click(on_element=None)

鼠标左点击元素.

**Parameters**

*on_element*: 点击元素. 如果无参数，则点击当前鼠标的位置.

#### click_and_hold(on_element=None)

对一个元素点击且不释放，一直点着.

**Parameters**

*on_element*: 点击元素不释放. 如果无参数，则点击当前鼠标的位置.

#### context_click(on_element=None)

上下文单机（右击）一个元素.

**Parameters**

*on_element*: 上下文单机（右击）一个元素. 如果无参数，则点击当前鼠标的位置.

#### double_click(on_element=None)

双击元素.

**Parameters**

*on_element*: 双击元素，如果无参数，则点击当前鼠标的位置.

#### drag_and_drop(source, target)

鼠标左键点击source元素不释放，移动到target元素，然后释放鼠标.

**Parameters**

*source*: 传入起点元素`WebElement`
*target*: 传入终点元素`WebElement`

**Example**

```python
actions = ActionChains(driver)
from_element = driver.find_element_by_id("source")
to_element = driver.find_element_by_id("target")
actions.drag_and_drop(from_element, to_element).perform()
```



#### drag_and_drop_by_offset(source, xoffset, yoffset)

鼠标左键点击source元素不释放，移动到坐标位置，然后释放鼠标..

**Parameters**

*source*: 传入起点元素`WebElement`.
*xoffset*: 传入终点的X坐标.
*yoffset*: 传入终点的Y坐标.

#### key_down(value, element=None)

按键不释放，通常用作Control, Alt and Shift.

**Parameters**

*value*: 键值. Keys class 定义的所有值.
*element*: 对某元素使用按键. 如果无参数，则对当前聚焦的元素使用.

**Example**

```python
actions = ActionChains(driver)
# 全选复制,全选，复制
actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
```



#### key_up(value, element=None)

释放按键，与`key_down`类似，一个按下，一个释放.

#### move_by_offset(xoffset, yoffset)

移动鼠标到坐标位置.

**Parameters**

*xoffset*: 坐标的X轴值，整数.
*yoffset*: 坐标的Y轴值，整数.

#### move_to_element(to_element)

将鼠标移动到元素的中间，常用在鼠标悬浮时选择子菜单。

**Parameters**

*to_element*: 传入元素`WebElement`.

**Example**

#### move_to_element_with_offset(to_element, xoffset, yoffset)

按指定元素的偏移量移动鼠标，偏移量相对于元素的左上角

**Parameters**

*to_element*: 传入 `WebElement`.
*xoffset*: 偏移量X.
*yoffset*:  偏移量Y.

#### pause(seconds)

停顿特定的时间.

#### perform()

执行所有储存的动作.

#### release(on_element=None)

释放元素上的鼠标按钮.

**Parameters**

*on_element*: 如果无参，则在当前鼠标位置释放.

#### reset_actions()

清除已在本地和远程端存储的操作.

#### send_keys(keys_to_send)

向当前焦点元素发送键.

**Parameters**

*keys_to_send*: Keys中定义的所有值

#### send_keys_to_element(element, keys_to_send)

向元素发送键.

**Parameters**

*element*: 传入 `WebElement`.
*keys_to_send*: Keys中定义的所有值

### 常见的场景

#### 打开新的窗口

按住`Ctrl` 点击链接，会在浏览器中新打开一个tab。按住`Shift` 点击链接，会新打开一个浏览器实例

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

base_url = "http://lucas234.gitee.io/static-demo/"
chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
actions = ActionChains(driver)
# 新tab 页面打开链接, 另起一个窗口打开链接
link = driver.find_element_by_id('drag_and_drop')
actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
# 在 mac 上
actions.key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
actions.key_down(Keys.SHIFT).click(link).key_up(Keys.SHIFT).perform()
```

#### 鼠标悬浮点击子菜单

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

base_url = "http://lucas234.gitee.io/static-demo/"
chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
actions = ActionChains(driver)
# 悬浮显示子菜单,选择子菜单
driver.find_element_by_id("dropdownlist").click()
menu_element = driver.find_element_by_class_name('dropbtn')
sub_element = driver.find_element_by_xpath('//a[text()="Link 2"]')
actions.move_to_element(menu_element).click(sub_element).perform()
```

#### 拖拽

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

base_url = "http://lucas234.gitee.io/static-demo/"
chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
actions = ActionChains(driver)
# 拖拽
driver.find_element_by_id('drag_and_drop').click()
from_element = driver.find_element_by_id("square")
to_element = driver.find_element_by_id("target")
ActionChains(driver).pause(1).drag_and_drop(from_element, to_element).perform()
```

#### 全选复制

```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

base_url = "http://lucas234.gitee.io/static-demo/"
chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
actions = ActionChains(driver)
# 全选复制,全选，复制
actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
```

## 二、模拟键盘输入

send_keys()方法可以用来模拟键盘输入，参数是Keys定义的所有键值， 甚至是组合键， 如 Ctrl+A、 Ctrl+C 等

常用的键盘操作：

- send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
- send_keys(Keys.SPACE) 空格键(Space)
- send_keys(Keys.TAB) 制表键(Tab)
- send_keys(Keys.ESCAPE) 回退键（Esc）
- send_keys(Keys.ENTER) 回车键（Enter）
- send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
- send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
- send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
- send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
- send_keys(Keys.F1) 键盘 F1
- ……
- send_keys(Keys.F12) 键盘 F12

例子：

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

base_url = "https://www.baidu.com/"
chrome_driver_path = r"C:\diy\your path\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(base_url)
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
```

## 参考

[https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#module-selenium.webdriver.common.action_chains](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html#module-selenium.webdriver.common.action_chains)

[https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.keys.html#module-selenium.webdriver.common.keys)