1. unknown server

   > org.openqa.selenium.WebDriverException: An unknown server-side error occurred while processing the command. Original error: Error getting device platform version. Original error: Error executing adbExec. Original error: 'Command 'C\:\\Users\\liul5\\AppData\\Local\\Android\\Sdk\\platform-tools\\adb.exe -P 5037 -s 520381b347dd148b shell getprop ro.build.version.release' timed out after 20000ms'; Stderr: ''; Code: 'null' (WARNING: The server did not provide any stacktrace information)Command duration or timeout: 40.88 seconds

   方法：1. 卸载app上的appium server；2. `admin`权限启动`appium`

2. 用这种定位时`uiAutomator = "new UiSelector().text(\"Tag 1\")"`

   不能用单引号代替,用单引号会报错`uiAutomator = "new UiSelector().text('Tag 1')"`

3. 输入框不能输入字符时，用ID定位报这种错的

   > （StaleObjectException）：[element.sendKeys("1233")] Error response status: 10, StaleElementReference - An element command failed because the referenced element is no longer attached to the DOM. Selenium error: android.support.test.uiautomator.StaleObjectException at android.support.test.uiautomator.UiObject2.getAccessibilityNodeInfo(UiObject2.java:629) at android.support.test.uiautomator.UiObject2.getText(UiObject2.java:284) at

   方法：可以用`uiAutomator`的方式定位，`new UiSelector().text("something") `即可

4. iOS，Xcode的版本不同所对应的元素可能不同
   
5. 每次连接一个设备(如果该设备上有已经生成相应的文件`io.appium.uiautomator2.server`、`io.appium.uiautomator2.server.test`), 则需要将其卸载后,重启server,才可以运行脚本,不然会报错(类似于server-side的错误)
   
6. `Android`模拟器和`Windows docker`只能使用一个，`docker` 需要`Hyper-V` 而 `Android`模拟器不能有

 