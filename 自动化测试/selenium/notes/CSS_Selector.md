`css selector` 通常有以下几种方式确定元素：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200509160411484.png#pic_center)

下文所涉及的HTML代码：

```html
<!DOCTYPE html>
<html>
<head>
	<titile>Css selector 说明</title>
	<style>
		div{width: 100%;line-height:20px;
			margin-top:10px;background-color:orange;}
			
		/* [id]{background-color: red;} */
		
		[id="two"]{background-color: blue;}
		[class~="c2"]{font-size: 36px;color:white; background-color: yellow;}
		[class|="five"]{font-size: 36px;color:white; background-color: gray;}
		[id^="six"]{font-size: 36px;color:white; background-color: pink;}
		[id$="ree"]{background-color:steelblue;} 
	</style>

</head>
<body>
	<div id='one'>1</div>
	<div id='two'>2</div>
	<div id="three">3</div>
	<div id="c1 c2 c3" id="four">4</div>
	<div class="five-test">5</div>
	<div id="six test">6</div>
	<div> 
		<label class="hidden-label" for="Email">Test ID selector: </label>
		<input id="Email" type="email" autofocus="" placeholder="Enter your email" name="Email" spellcheck="false" value=""> 
	</div>
	<div> 
		<label class="hidden-label" for="Email">Test Class selector: </label>
		<input id="Passwd-hidden" class="password" type="password" spellcheck="false"> 
	</div>
	<div>
		<label class="hidden-label" for="Test attribute">Test attribute: </label>
		<input id="Test_attribute" class="inputtext" type="test email" tabindex="1" value="" name="test email">
	</div>
	<div>
		<label class="hidden-label" for="Test SUB-STRING MATCHES">Test SUB-STRING MATCHES: </label>
		<input id="Test_ID_001" >
	</div>
	<div id="buttonDiv" class="small">
		<label class="hidden-label" for="Test SUB-STRING MATCHES">Test Child Elements: </label>
		<input id="Child Elements" >
	</div>
	<div>
		<label class="hidden-label" for="Test nth-child">Test nth-child: </label>
		<ul id="automation">
		   <li>Selenium</li>
		   <li>Appium</li>
		   <li>Sikuli</li>
		</ul>
	</div>
	<div>
		<label class="hidden-label" for="Test inner-STRING">Test inner-STRING MATCHES: </label>
		<button id="test-button" ><span>test1_button</span></button>
		<button id="test2-button" ><span>test2_button</span></button>
	</div>
	<div><a herf="just a test">link</a></div>
</body>
</html>
```

测试Python代码（将上边代码保存为 `test_css_selector.html`）：

```python
dr = webdriver.Chrome(r"your path/chromedriver.exe")
# 将上边代码保存为 test_css_selector.html
dr.get(r"file:///your path/test_css_selector.html")
dr.find_element_by_css_selector("input#Email").send_keys("test ID selector")
# dr.find_element_by_css_selector("#Email").send_keys("test ID selector")
# dr.find_element_by_css_selector("input.password").send_keys("test class selector")
dr.find_element_by_css_selector(".password").send_keys("test class selector")
```



#### ID 选择器

在CSS中，`#`表示选择ID属性，语法为：`css=<HTML tag><#><ID属性值>`或 `css=<#><ID属性值>`；例子：`css="input#Email"` 或 `css="#Email"`

HTML：

```html
<div> 
    <label class="hidden-label" for="Email">Test ID selector: </label>
    <input id="Email" type="email" autofocus="" placeholder="Enter your email" name="Email" spellcheck="false" value=""> 
</div>
```

代码：

```python
# python 代码
dr.find_element_by_css_selector("input#Email").send_keys("test ID selector")
# dr.find_element_by_css_selector("#Email").send_keys("test ID selector")
# Java 代码
# driver.findElement(By.cssSelector("input#Email"));
# driver.findElement(By.cssSelector("#Email"));
```

#### Class 选择器

在CSS中，`.`表示选择class属性，语法为：`css=<HTML tag><.><class属性值>`或 `css=<.><class属性值>`；例子：`css="input.password"` 或 `css=".password"`

HTML：

```html
<div> 
    <label class="hidden-label" for="Email">Test Class selector: </label>
    <input id="Passwd-hidden" class="password" type="password" spellcheck="false"> 
</div>
```

代码：

```python
# python 代码
dr.find_element_by_css_selector("input.password").send_keys("test class selector")
# dr.find_element_by_css_selector(".password").send_keys("test class selector")
# Java 代码
# driver.findElement(By.cssSelector("input.password"));
# driver.findElement(By.cssSelector(".password"));
```

#### 

#### Attribute 和Sub-String 选择器

属性选择器说明如下：

| 选择器类型      | 选择器说明                                                   |
| :-------------- | :----------------------------------------------------------- |
| `[attr]`        | 表示选择带有attr命名属性的所有元素                           |
| `[attr=value]`  | 表示选择带有attr命名属性，且属性值为value的元素              |
| `[attr~=value]` | 表示选择带有attr命名的属性，且该属性是一个一空格作为分隔符的值列表，至少有一个值为value |
| `[attr|=value]` | 表示选择以attr命名属性，且属性值为value或者以value-为前缀开头 |
| `[attr^=value]` | 表示带有以attr命名的属性，且属性值是以value开头的元素        |
| `[attr$=value]` | 表示带有以attr命名的属性，且属性值是以value结尾的元素        |
| `[attr*=value]` | 表示带有以attr命名的属性，且属性值包含有value的元素          |

默认代码：

```html
<!DOCTYPE html>
<html>
<head>
	<titile>Css selector 说明</title>
	<style>
		div{width: 100%;line-height:40px;
			margin-top:20px;background-color:orange;}
	</style>
</head>
<body>
	<div id='one'>1</div>
	<div id='two'>2</div>
	<div id="three">3</div>
	<div class="c1 c2 c3" id="four">4</div>
	<div class="five-test">5</div>
	<div id="six test">6</div>
</body>
</html>
```

效果图：

![](https://img-blog.csdnimg.cn/20200509160446113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70#pic_center)

修改style代码如下：

```html
	<style>
        div{width: 100%;line-height:40px;
            margin-top:20px;background-color:orange;}
        [id]{background-color: red;}
        [id="two"]{background-color: blue;}
        [class~="c2"]{font-size: 36px;color:white; background-color: yellow;}
        [class|="five"]{font-size: 36px;color:white; background-color: gray;}
        [id^="six"]{font-size: 36px;color:white; background-color: pink;}
        [id$="ree"]{background-color:steelblue;} 
	</style>
```

修改后的效果图：

![](https://img-blog.csdnimg.cn/20200509160502920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70#pic_center)

在CSS中，Attribute 选择器的语法可参考上边的说明，`css=input[id='Test attribute']`：

HTML：

```html
<div id="c1 c2 c3" id="four">4</div>
<div class="five-test">5</div>
<div>
    <label class="hidden-label" for="Test attribute">Test attribute: </label>
    <input id="Test attribute" class="inputtext" type="test email" tabindex="1" value="" name="test email">
</div>
<div>
    <label class="hidden-label" for="Test SUB-STRING MATCHES">Test SUB-STRING MATCHES: </label>
    <input id="Test_ID_001" >
</div>
<div>
    <label class="hidden-label" for="Test nth-child">Test nth-child: </label>
    <ul id="automation">
        <li>Selenium</li>
        <li>Appium</li>
        <li>Sikuli</li>
    </ul>
</div>
```

代码：

```python
dr.find_element_by_css_selector("input[type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input[id='Test_attribute'][type='test email']").send_keys("test attribute selector")
# dr.find_element_by_css_selector("input#Test_attribute[type='test email']").send_keys("test attribute selector")
#dr.find_element_by_css_selector("input.inputtext[type='test email']").send_keys("test attribute selector")
# sub-string
dr.find_element_by_css_selector("input[id^='Test_I']").send_keys("test sub-string selector")
# dr.find_element_by_css_selector("input[id$='001']").send_keys("test sub-string selector")
#dr.find_element_by_css_selector("input[id*='ID']").send_keys("test sub-string selector")
# print(dr.find_element_by_css_selector("div[id~='c2']").text)
# print(dr.find_element_by_css_selector("div[class|='five']").text)
# 选择id值包含Test且不包含attribute的属性
dr.find_element_by_css_selector("input[id*='Test']:not([id*='attribute'])").send_keys("test contains sub-string selector")
# 定位子元素
dr.find_element_by_css_selector("div#buttonDiv input").send_keys("test child element")
# 定位多个子元素
print(dr.find_element_by_css_selector("ul#automation li:last-child").text)
print(dr.find_element_by_css_selector("ul#automation li:nth-of-type(2)").text)
# 也可以直接用[attribute=value]进行定位
print(dr.find_element_by_css_selector("[id='two']").text)
print(dr.find_element_by_css_selector("[id^='tw']").text)

```

#### Inner-String 选择器

语法：`css=tag:contains("inner text")`，但是经过试验，不能用，貌似已经弃用这种方法了，会提示错误：`invalid selector: An invalid or illegal selector was specified`，没办法只能用`xpath`了

## 参考：

[https://www.w3.org/TR/CSS21/selector.html%23id-selectors](https://www.w3.org/TR/CSS21/selector.html%23id-selectors)

[https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)

[https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity)

[https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048](https://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048)

[https://www.w3school.com.cn/cssref/css_selectors.asp](https://www.w3school.com.cn/cssref/css_selectors.asp)