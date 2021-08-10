### appium 定位方式种类：

|方式| 注释 |
|:----|:----|
| AccessibilityId|在 Android 上，主要使用元素的content-desc属性，如该属性为空，不能使用此定位方式。在 iOS 上，主要使用元素的accessibility id属性进行定位，如该属性为空，如该属性为空,不能使用该属性。  |
| Id|使用元素的Resource Id属性定位，支持：Android，仅支持 Android 4.3或以上，推荐使用  | 
| name|使用元素的name属性定位，推荐使用  | 
| Xpath| 支持：Android 和 iOS。但由于 iOS 10开始使用的 XCUITest 框架原声不支持，定位速度很慢，所以官方现在不推荐大家使用，也有其他替代的定位方式可使用  |   
| className |使用元素的className属性定位，支持：Android 和 iOS，推荐使用  |  
| AndroidUIAutomator| 仅支持 Android 4.2或以上，可支持元素的单个属性和多个属性定位，推荐使用 |   
| iOSNsPredicateString| 仅支持 iOS 10或以上，可支持元素的单个属性和多个属性定位，推荐使用。 |  
| iOSClassChain| 仅支持 iOS 10或以上，这是 github 的 Mykola Mokhnach 大神开发，仅限在 WebDriverAgent 框架使用，用于替代 xpath 的 |   
| IosUIAutomation| 仅支持 iOS 9.3或以下，是 iOS 旧框架 UIAutomation 的定位方式，现在基本上很少使用，这个定位类型同样可使用 iOS 谓词进行定位，详细可参考：iOSNsPredicate |  
| windowsAutomation | windows自动化定位方式 |  

### 元素定位使用样例
###### AccessibilityId

```java
// java
driver.findElementByAccessibilityId("username")；
driver.findElement(MobileBy.AccessibilityId("username"))
// python
driver.find_element_by_accessibility_id("slider")
```

###### Id
```java
// java
driver.findElementById("username")；
driver.findElement(MobileBy.id("username"))
// python
driver.find_element_by_id("slider")
```
###### name
```java
// java
driver.findElementByName("username")；
driver.findElement(MobileBy.name("username"))
// python
driver.find_element_by_name("slider")
```
###### Xpath
```java
// java
driver.findElementByXpath("	/hierarchy/android.widget.FrameLayout[1]/android.widget.TextView")；
driver.findElement(MobileBy.xpath("/hierarchy/android.widget.FrameLayout[1]/android.widget.TextView"))
//1.使用绝对路径定位，
MobileBy.xpath("XCUIElementTypeWindow/XCUIElementTypeAny[3]")
//2.使用相对路径定位
MobileBy.xpath("//className")
//3.通过元素的索引定位
MobileBy.xpath("//className[2]")
//4.通过元素的属性定位
MobileBy.xpath("//XCUIElementTypeTable[@name=\"table\"]") //一种属性
MobileBy.xpath("//className[@label='购物'][@isVisible='0']") //两种属性
MobileBy.xpath("//className[contains(@label,'购')]") //部分属性

// python
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout[1]/android.widget.TextView")
```

###### className 
```java
// java
driver.findElementByClassName("username")；
driver.findElement(MobileBy.className("username"))
// python
driver.find_element_by_class_name("slider")
```

###### AndroidUIAutomator
```java
// java
driver.findElementByAndroidUIAutomator("new UiSelector().text(\"username\")");	
driver.findElement(MobileBy.AndroidUIAutomator("new UiSelector().text(\"username\")"))
// python
driver.find_element_by_android_uiautomator("new UiSelector().text(\"username\")")
```
**UiSelector的基本方法:**

1. text(String text) 文本
	```java
	// 对应属性text
	new UiSelector().text("username")
	```

2. textContains(String text) 文本包含

	```java
	new UiSelector().textContains("username")
	```
3. textMatches(String regex) 文本正则表达式匹配
	```java
	new UiSelector().textMatches("^Add.*")
	//匹配 Add note
	```

4. textStartsWith(String text) 文本开始字符
	```java
	new UiSelector().textStartsWith("Add")
	//匹配 Add note
	```
5. description(String desc) 描述
	```java
	// 对应属性content-desc
	new UiSelector().description("username")
	```
6. descriptionContains(String desc) 描述包含
	```java
	// 对应属性content-desc
	new UiSelector().descriptionContains("username")
	```
7. descriptionMatches(String regex) 描述正则
	```java
	// 对应属性content-desc
	new UiSelector().descriptionMatches("username")
	```
8. descriptionStartsWith(String desc) 描述开始字符
	```java
	// 对应属性content-desc
	new UiSelector().descriptionStartsWith("username")
	```
9. resourceId(String id) 资源id
	```java
	new UiSelector().resourceId("android:id/title")
	```
10. resourceIdMatches(String regex) 资源ID正则
	```java
	new UiSelector().resourceIdMatches(".+id/title")
	```
11. childSelector(UiSelector selector) 子类
	```java
	new UiSelector().className("android.view.View").childSelector(new UiSelector().text("Save"))
	```

12. className(String  className) 类名
	```java
	new UiSelector().className("android.widget.TextView")
	```
13. classNameMatches方法 
	```java
	new UiSelector().classNameMatches(".*TextView$")
	```
14. index(int index) 编号
	```java
	//根据属性index编号
	new UiSelector().index(7).clickable(true).resourceId("com.snapdeal.main:id/sort_by_text_view")
	```
15. instance(int instantce) 索引
	```java
	//相同的resourceId，按索引选取第一个元素
	new UiSelector().resourceId("com.snapdeal.main:id/icon").instance(0)
	```
16. 如果多个属性判断，则直接在后边添加即可
	```java
	//使用两种属性定位
	new UiSelector().text("login").clickable(true)
	```
	
17. 详情参考：[UiSelector](https://developer.android.com/reference/android/support/test/uiautomator/UiSelector)

###### iOSNsPredicateString / IosUIAutomation
一般通过type、value、name、label、enabled、visible这些属性判断，具体根据实际属性值
元素的定位方式都是一个属性+运算符+值形式存在
1. 比较运算符：`>, <, ==, >=, <=, !=`
可用于数值和字符串的比较，
如：`name>100` 或 `name == '测试'`

2. 范围运算符：`IN, BETWEEN`
可用于数值和字符串的范围核对
如：`name BETWEEN {3,10}，name IN {'Alan','May'}`

3. 字符串相关：`CONTAINS、BEGINSWITH、ENDSWITH`
包含某个字符串，如：`label CONTAINS '测试'`
以某个字符串开头，如：`label BEGINSWITH '420'`
以某个字符串结束，如：`label ENDSWITH '班级群'`
PS：在三个关键字后加上`[c]`不区分大小写，可用于字母的校验；`[d]`不区分发音符号，即没有重音符号`($、#、%等)`；`[cd]`即不区分大小写，也不区分发音符号，如：`name CONTAINS[c] ABcd`和`name CONTAINS abcd`、`name CONTAINS ABCD`是等同的，注意后面两个没带`[c]`的不相等

4. 通配符：`LIKE`
通配符也接受`[cd]，?`代表一个字符，`*`代表多个字符
如：一个元素的label属性为
	```
	label LIKE '420测试班级群'
	label LIKE '420测?班级群'
	label LIKE '420??班级群'
	label LIKE '42？测试班？群'
	label LIKE '*试班级群'
	label LIKE '420测试班*'
	label LIKE '42*级群'
	label LIKE '4*试*群'
	```
	以上这么多种文本都可以被识别为同一个元素。

5. 正则表达式：`MATCHES`
如：以4开头，以群结束，
`label MATCHES '^4.+群$'`

	```java
	// java
	driver.findElementsByIosNsPredicate("label == 'Cancel' AND visible = false");	
	driver.findElement(MobileBy.iOSNsPredicateString("label == 'Cancel' AND visible = false")
	driver.findElement(MobileBy.IosUIAutomation("label == 'Cancel' AND visible = false")
	
	// python
	driver.find_element_by_ios_predicate("label == 'Cancel' AND visible = false")
	driver.find_element_by_ios_uiautomation("label == 'Cancel' AND visible = false")
	```
###### iOSClassChain
具体规则参考：[参考1](https://pavankovurru.github.io/Appium_Mobile_Automation_Framework/documents/README_IOS.html)，[参考2](https://github.com/facebookarchive/WebDriverAgent/wiki/Class-Chain-Queries-Construction-Rules)，[参考3](https://github.com/appium/appium-xcuitest-driver/pull/391)
```java
// java
driver.findElementByIosClassChain("XCUIElementTypeWindow/XCUIElementTypeAny[3]");	
driver.findElement(MobileBy.iOSClassChain("XCUIElementTypeWindow/XCUIElementTypeAny[3]")

// python
driver.find_element_by_ios_class_chain("XCUIElementTypeWindow/XCUIElementTypeAny[3]")
```

### pagefactory模式元素定位
如果不应用于全平台（android、iOS、Windows、web）,则元素定义可以用`MobileElement`，否则需要用`WebElement`或者RemoteWebElement定义，详情参考：[参考](https://github.com/appium/java-client/blob/master/docs/Page-objects.md)

```java
	//list
    @AndroidFindBy(className = "android.widget.CheckedTextView")
    public List<WebElement> countryTab;
    
    @iOSXCUITFindBy(id = "Filter Publications")
    @WindowsFindBy(accessibility = "PasswordBox")
    @AndroidFindBy(xpath = "(//XCUIElementTypeStaticText[@name = \"test\"])[2]")
    public WebElement passwordBox;

    @AndroidFindBy(uiAutomator = "new UiSelector().text(\"login\")")
    @iOSFindBy(accessibility = "login")
    public List<WebElement> loginButton;
    
    @iOSXCUITFindBy(iOSNsPredicate = "label == 'test' AND visible = false")
    @AndroidFindBy(uiAutomator = "new UiSelector().className(\"android.widget.FrameLayout\").childSelector(new UiSelector().resourceId(\"android:id/button2\"))")
    public WebElement cancelButton;
	
	//使用HowToUseLocators定位元素，可以选择两种定位方式，默认先选择id = "test"进行查找元素，如果找到元素，则执行操作，不再进行第二种（uiAutomator）的方式了，未找到则用第二种方式定位元素（对于定位不稳定的元素，可以多几种方式来确保定位到元素）。
    @HowToUseLocators(androidAutomation = ALL_POSSIBLE)
    @AndroidFindBy(id = "test")
    @AndroidFindBy(uiAutomator = "new UiSelector().text(\"test\")")
    public MobileElement testLocator;

	//也可以显示的添加优先级,默认值为0，优先级最高
	@HowToUseLocators(androidAutomation = ALL_POSSIBLE)
    @AndroidFindBy(id = "test")
    @AndroidFindBy(uiAutomator = "new UiSelector().text(\"test\")"，priority = 1)
    @AndroidFindBy(xpath= "//test"，priority = 3)
    public MobileElement testLocator;

	@HowToUseLocators(androidAutomation = ALL_POSSIBLE, iOSAutomation =
	ALL_POSSIBLE)
	@FindAll{@FindBy(someStrategy1), @FindBy(someStrategy2)})
	@AndroidFindBy(fakeID1) @AndroidFindBy(someStrategy2)
	@iOSFindBy(fakeID1) @iOSFindBy(someStrategy2)
	public MobileElement someElement;

	// chain 模式，会先查找第一种定位策略，然后查找第二种，以下例子，如果运行android的APP，则先找@AndroidFindBy(parent)，然后再查找@AndroidFindBy(child)
	@FindBys({@FindBy(someStrategy1),
	@FindBy(someStrategy2)})
	@AndroidFindBy(parent)
	@AndroidFindBy(child)
	@iOSFindBy(parent)
	@iOSFindBy(child)
	public MobileElement someElement;

	// 也可以混合使用，如下的例子，android按照chain模式查找，iOS按照ALL_POSSIBLE模式查找
	@HowToUseLocators(androidAutomation = CHAIN, iOSAutomation = ALL_POSSIBLE)
	@FindAll{@FindBy(someStrategy1), @FindBy(someStrategy2)}) 
	@AndroidFindBy(someStrategy1) @AndroidFindBy(someStrategy2) 
	@iOSFindBy(someStrategy1) @iOSFindBy(someStrategy2) 
	public WebElement someElement;
```


### 参考
- [https://developers.perfectomobile.com/display/TT/Finding+Elements+on+XCUITest+devices](https://developers.perfectomobile.com/display/TT/Finding+Elements+on+XCUITest+devices)
- [https://github.com/facebookarchive/WebDriverAgent/wiki/How-To-Achieve-The-Best-Lookup-Performance](https://github.com/facebookarchive/WebDriverAgent/wiki/How-To-Achieve-The-Best-Lookup-Performance)
- [http://appium.io/docs/en/writing-running-appium/ios/ios-predicate/#ios-predicate](http://appium.io/docs/en/writing-running-appium/ios/ios-predicate/#ios-predicate)
- [https://blog.imaginea.com/usage-of-uiselector-mobileby-androiduiautomator/](https://blog.imaginea.com/usage-of-uiselector-mobileby-androiduiautomator/)