## Mac搭建Appium自动化测试环境

## 环境搭建列表
- 通用环境
	- Homebrew
	- Node & NPM
	- JDK
	- Carthage
	- Appium
	- Appium Doctor
- iOS 环境
	- Xcode
	- ios-deploy
	- ideviceinstaller & libimobiledevice
	- ios_webkit_debug_proxy
- Android 环境
	- android-sdk
	- platform-tools
	- build-tools
	- emulator
	
## 通用环境
#### Ⅰ 安装 Homebrew
Homebrew是一个包管理软件，它可以使我们更容易地安装其他一些软件，终端输入[安装](https://brew.sh/)：

```powershell
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

如果安装失败（网速不行等。。），可以打开网址：[https://raw.githubusercontent.com/Homebrew/install/master/install](https://raw.githubusercontent.com/Homebrew/install/master/install) 
将其内容保存为`homebrew.txt`（链接: [下载](https://pan.baidu.com/s/1kbIcopMxeuXusJflNbiSPw) 提取码: `8htr`），然后终端输入：

```powershell
/usr/bin/ruby homebrew.txt
```

此步骤还顺带安装了Xcode命令行工具。

#### Ⅱ 安装 Node & NPM
Node是一个javascript运行时环境，npm是节点包管理器。我们需要这些，因为Appium是一个节点应用程序。在终端中，输入以下命令(此命令也将安装npm)：

```powershell
brew install node
```
#### Ⅲ 安装 JDK
下载 [Java jdk](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) ，按步骤安装，安装完成后需要在`.bash_profile`设置 `JAVA_HOME` ，设置之前你可以通过下边的命令查看Java的安装路径，terminal输入：

```powershell
/usr/libexec/java_home --v
```

输出路径：

`/Library/Java/JavaVirtualMachines/jdk1.8.0_171.jdk/Contents/Home`

通过`vim` 编辑`.bash_profile`文件，终端输入：

```powershell
vim ~/.bash_profile
```

按 `i`键进入编辑模式，移动到最下边加入如下两行（路径为之前查看的）：

```powershell
# [改为你自己的java_home路径]
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_171.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH
```
添加后按 `Esc`按键，输入`:wq`保存并退出编辑。输入使其生效（或重启终端）：

```powershell
source  ~/.bash_profile
```


#### Ⅳ 安装 Carthage
Carthage是一个依赖管理器，`WebDriverAgent`需要它，终端输入：

```powershell
brew install carthage
```

#### Ⅴ 安装 Appium 
Appium（Version 1.15.1）是一个用于本地、混合和移动web应用程序的开源测试自动化框架。它使用WebDriver协议驱动iOS、Android和Windows mobile应用程序。终端安装server版输入：

```powershell
# 安装 server 版
npm install -g appium
```

默认安装最新的版本，如果想安装指定的版本：

```powershell
npm install -g appium@1.7.2
```
卸载 Appium: 

```powershell
npm uninstall -g appium
npm cache clean --force
```

安装桌面版（因为桌面版方便元素定位），[下载](https://github.com/appium/appium-desktop/releases/tag/v1.15.1) 相应的版本进行安装（安装两种方式，方便使用）。

#### Ⅵ 安装 Appium Doctor
Appium doctor是一个小型软件，它检查Appium成功运行的所有(几乎所有)前提条件。终端输入：

```powershell
npm install -g appium-doctor
```

appium-doctor的输出应该是这样的:

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191223162823920.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)
## IOS
#### Ⅶ 安装Xcode和模拟器
启动Mac应用程序商店并下载/安装Xcode（Version 10.1）。安装之后，启动Xcode并选择
`Xcode > Preferences > Components`  来安装可能想要测试的模拟器。

> 如果已经安装过xcode，appium-doctor提示未安装，则运行命令即可：
> sudo xcode-select -r


`Tips`: 

```powershell
# 查看已启动的模拟器udid
xcrun simctl list | grep '(Booted)'  
# 列出所有设备，包括真机、模拟器、mac
instruments -s devices 
#录像 
xrecord --quicktime --list
xrecord --quicktime --name="iPhone" --out="/Users/blah/video/iphone.mp4" --force
```
模拟器相关命令参考：[这里](https://blog.csdn.net/lb245557472/article/details/89493199)


#### Ⅷ 安装 libimobiledevice & ideviceinstaller
`libimobiledevice` 是一个跨平台的软件库，支持 iPhone®, iPod Touch®, iPad® and Apple TV® 等设备的通讯协议。不依赖任何已有的私有库，不需要越狱。应用软件可以通过这个开发包轻松访问设备的文件系统、获取设备信息，备份和恢复设备，管理 SpringBoard 图标，管理已安装应用，获取通讯录、日程、备注和书签等信息，使用 libgpod 同步音乐和视频。
`ideviceinstaller` 是一个与iOS设备的installation_proxy交互的工具，允许安装、升级、卸载、存档、还原和列举已安装或存档的应用程序。此工具用于在真机上运行测试，默认是都安装的。

```powershell
brew install libimobiledevice --HEAD   # 安装最新的更新，支持 iOS 10
brew install ideviceinstaller  # 仅在 iOS9工作
```
如果安装时遇到： "invalid active developer path" 则运行：

```powershell
xcode-select --install
sudo xcode-select -r
```

>问题
> dyld: Library not loaded:  /usr/local/opt/openssl/lib/libssl.1.0.0.dylib   Referenced from: 
> /usr/local/opt/libimobiledevice/lib/libimobiledevice.6.dylib   Reason: image not found
> 如果遇到如上错误，则先卸载`ideviceinstaller 和 libimobiledevice`（`brew uninstall  ideviceinstaller` ,`brew uninstall  libimobiledevice`），然后再重安装即可


`Tips`: 
1. 获取设备的udid

	```powershell
	idevice_id --list  	# 略写为 -l 显示当前所连接设备的 udid
	idevice_id -l      # 显示当前所连接的设备[udid]，包括 usb、WiFi 连接
	instruments -s devices  # 列出设备包括模拟器、真机及 mac 电脑本身
	ideviceinfo   #  可以在返回的数据中找到 udid
	# 苹果手机 safari打开网址http://fir.im/udid 就看到了	
	```

2. 安装应用

	```powershell
	# xxx.ipa为应用在本地的路径
	ideviceinstaller -i apppath # 安装apppath下的app
	ideviceinstaller -u [udid] -i [xxx.ipa] # 给指定连接的设备安装应用
	```

3. 卸载应用

	```powershell
	# bundleId为应用的包名
	ideviceinstaller -u [udid] -U [bundleId] # 给指定连接的设备卸载应用
	```

4. 查看设备已安装的应用

	```powershell
	ideviceinstaller -l  #列出手机上所有用户安装的app
	# 运行某个app
	idevicedebug run 'APP_BUNDLE_ID'  # 可以直接launch某个app，当然，这个app必须是你通过development证书build到手机上的才行
	ideviceinstaller -u [udid] -l                   # 指定设备，查看安装的第三方应用
	ideviceinstaller -u [udid] -l -o list_user      # 指定设备，查看安装的第三方应用
	ideviceinstaller -u [udid] -l -o list_system    # 指定设备，查看安装的系统应用
	ideviceinstaller -u [udid] -l -o list_all       # 指定设备，查看安装的系统应用和第三方应用
	```

5. 获取设备信息

	```powershell
	ideviceinfo -u [udid]                       # 指定设备，获取设备信息
	ideviceinfo -u [udid] -k DeviceName         # 指定设备，获取设备名称：iPhone6s
	idevicename -u [udid]                       # 指定设备，获取设备名称：iPhone6s
	ideviceinfo -u [udid] -k ProductVersion     # 指定设备，获取设备版本：10.3.1
	ideviceinfo -u [udid] -k ProductType        # 指定设备，获取设备类型：iPhone8,1
	ideviceinfo -u [udid] -k ProductName        # 指定设备，获取设备系统名称：iPhone OS
	```
6. 其他系统文件信息

	```powershell
	idevicescreenshot # 截图
	ideviceinfo  # 获取设备所有信息
	idevicesyslog  # 获取设备日志
	idevicecrashreport -e test  # 获取设备 crashlog，test 是文件夹需新建
	idevicediagnostics  restart  # （shutdown、sleep）管理设备状态 - 重启、关机、睡眠等
	```

#### Ⅸ 安装 ios-deploy
`ios-deploy` 同样是一个不需要用Xcode安装和调试应用的命令行工具。需要一个有效的开发者证书，需要 Xcode 7以上的版本。终端输入：

```powershell
brew install ios-deploy
```
`Tips`:
1.  安装应用

	```powershell
	ios-deploy -c  # 查看当前链接的设备，获取udid
	# xxx.app为 Xcode 编译后的应用安装包路径
	ios-deploy --id [udid] --bundle [xxx.app] # 给指定应用安装应用
	```

2. 卸载应用

	```powershell
	ios-deploy --id [udid] --uninstall_only --bundle_id [bundleId] # 给指定连接的设备卸载应用
	```

3. 查看设备已安装的应用

	```powershell
	ios-deploy --id [udid] --list_bundle_id     # 查看设备安装的所有应用，包括系统应用和第三方应用
	ios-deploy --id [udid] --exists --bundle_id     # 指定设备检查指定应用是否已经安装
	```

#### Ⅹ 安装 ios_webkit_debug_proxy
Appium使用`ios_webkit_debug_proxy`这个工具在真机上访问`web view`。在终端中，运行以下命令：

```powershell
brew install ios-webkit-debug-proxy
```
至此iOS环境搭建完毕！！！只适用于模拟器，真机的话还需要配置。

#### Ⅺ iOS真机手动配置
 查看`appium`的安装位置，正常npm安装的位置应该在`/usr/local/bin/appium`下
```powershell
which appium
# /usr/local/bin/appium
```
命令行安装的appium一般安装在`/usr/local/bin/appium`下，`WebDriverAgent`将会在路径：`/usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/` 下；如果是桌面版的，`WebDriverAgent`的路径是：`/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/` 

```powershell
# 命令行版
cd  /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/
# 桌面版
cd /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/
```
首先查看路径（`/usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent`）下有没有`WebDriverAgent.xcodeproj`（有的话跳过下边，直接用Xcode打开即可），没有的话直接打开终端运行如下命令搭建项目：

```powershell
cd /usr/local/lib/node_modules/appium/node_modules/appium-xcuitest-driver/WebDriverAgent/
mkdir -p Resources/WebDriverAgent.bundle
./Scripts/bootstrap.sh -d
```
然后用Xcode 打开 `WebDriverAgent.xcodeproj`，在 "General"  下将 `WebDriverAgentLib` 和 `WebDriverAgentRunner`设置成 "Automatically manage signing" 并在 "Team" 中选择你的开发团队 ；

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019122715583510.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

Xcode可能无法为WebDriverAgentRunner目标创建配置文件（Failed to create...）

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227155857465.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

这需要手动更改目标的`bundle id`，方法是进入“Build Settings”选项，更改“Product bundle Identifier”的值使Xcode将接受，默认为`com.facebook.WebDriverAgentRunner`
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227155955891.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)
返回  "General" 选项，看到对于文件`WebDriverAgentRunner`的配置文件已经创建成功了

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227160240816.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

最后，`build`项目：
通过Xcode获取`udid`：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227161506582.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2019122716152492.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

```powershell
# 利用ios-deploy获取，其他参考上边的介绍
ios-deploy -c 
cd /usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent
xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' test
```
即：

```powershell
xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=1A7A0E9D-98AE-4230-BC92-13F66901FCBA' test
```
最终看到这样输出就是成功了：

> Test Suite 'All tests' started at 2017-01-23 15:49:12.585
>     Test Suite 'WebDriverAgentRunner.xctest' started at 2017-01-23 15:49:12.586
>     Test Suite 'UITestingUITests' started at 2017-01-23 15:49:12.587
>     Test Case '-[UITestingUITests testRunner]' started.
>         t =     0.00s     Start Test at 2017-01-23 15:49:12.588
>         t =     0.00s     Set Up

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019122716051328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

验证是否安装成功，确保手机和电脑连接同一个WiFi（同一局域网内）：

```powershell
export DEVICE_URL='http://<device IP>:8100'
export JSON_HEADER='-H "Content-Type: application/json;charset=UTF-8, accept: application/json"'
curl -X GET $JSON_HEADER $DEVICE_URL/status
```
将会看到类似的输出：

```yaml
{
      "value" : {
        "state" : "success",
        "os" : {
          "name" : "iOS",
          "version" : "10.2"
        },
        "ios" : {
          "simulatorVersion" : "10.2",
          "ip" : "192.168.0.7"
        },
        "build" : {
          "time" : "Jan 23 2017 14:59:57"
        }
      },
      "sessionId" : "8951A6DD-F3AD-410E-A5DB-D042F42F68A7",
      "status" : 0
    }
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227160731124.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

然后会看到真机上安装了`WebDriverAgentRunner`应用：

![图](https://img-blog.csdnimg.cn/20191227160852712.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

安装成功后运行如果遇到这样的错误：

```python
2017-01-24 09:02:18.358 xcodebuild[30385:339674] Error Domain=com.apple.platform.iphoneos Code=-12 "Unable to launch com.apple.test.WebDriverAgentRunner-Runner" UserInfo={NSLocalizedDescription=Unable to launch com.apple.test.WebDriverAgentRunner-Runner, NSUnderlyingError=0x7fa839cadc60 {Error Domain=DTXMessage Code=1 "(null)" UserInfo={DTXExceptionKey=The operation couldn’t be completed. Unable to launch com.apple.test.WebDriverAgentRunner-Runner because it has an invalid code signature, inadequate entitlements or its profile has not been explicitly trusted by the user. : Failed to launch process with bundle identifier 'com.apple.test.WebDriverAgentRunner-Runner'}}}
2017-01-24 09:02:18.358 xcodebuild[30385:339674] Error Domain=IDETestOperationsObserverErrorDomain Code=5 "Early unexpected exit, operation never finished bootstrapping - no restart will be attempted" UserInfo={NSLocalizedDescription=Early unexpected exit, operation never finished bootstrapping - no restart will be attempted}

Testing failed:
    Test target WebDriverAgentRunner encountered an error (Early unexpected exit, operation never finished bootstrapping - no restart will be attempted)
```
问题是该应用在设备上不受信任。如果你手动尝试在设备上运行WebDriverAgent应用，你会看到一个弹出消息:

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191227161002273.png)

你可以通过Settings => General =>Device Management 来信任开发者并允WebDriverAgentRunner应用程序运行。
至此iOS真机运行环境配置完毕，你可以进行真机测试了~~

`Tips:`
<font color=red> 真机运行必须添加这两个参数：</font>

```python
  {	  
      # xcodeOrgId 类似：TEST INTERNATIONAL
      "xcodeOrgId": "<Team ID>",
      # xcodeSigningId是一个由Apple生成的唯一的10个字符的字符串，类似 6387P24J3L
      "xcodeSigningId": "iPhone Developer"
    }
```
这两个字段的获取方法：

![图](https://img-blog.csdnimg.cn/20191227161940979.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)


## Android 环境
安装Android环境可以使用直接使用 [Android studio](https://developer.android.com/studio/#downloads)来安装，但是会下载好多无用的东西，占用内存。可以选择下边的`Command line tools only`通过命令行安装（命令行安装可能会失败，多试几次就好）。这里只介绍用命令行安装的方法。

> 该方法会安装在 `/usr/local/Caskroom/android-sdk/4333796/` 目录下 `4333796`为android-SDK的版本号
>   该目录下要存在 tools、platform-tools、build-tools 三个文件夹，否则这个环境还是会存在问题的；  如果没有，需要运行安装、或移动 platform-tools 文件夹，可以将
> /usr/local/Caskroom/android-platform-tools/29.0.5/ 目录下的 platform-tools 文件夹复制过来

#### Ⅻ 安装 android-sdk
终端运行：

```powershell
brew cask install android-sdk
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191226133030175.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

#### XIII 安装 build-tools

```powershell
sdkmanager  --install  "build-tools;29.0.2"
```

#### XIV 安装 platform-tools
- sdkmanager 安装（`sdkmanager` 详细命令参考：[这里 ](https://developer.android.com/studio/command-line/sdkmanager)）
	```powershell
	# 使用sdkmanager 安装
	sdkmanager  --install  "platform-tools" "platforms;android-29"
	```

- 非 sdkmanager 安装
	```powershell
	# 如果上边的失败，则使用brew 安装（此安装完成后需要将platform-tools移
	# 动到 /usr/local/Caskroom/android-sdk/4333796/ 下）
	brew cask install android-platform-tools
	# 安装完成后移动
	mv /usr/local/Caskroom/android-platform-tools/29.0.5/platform-tools/  /usr/local/Caskroom/android-sdk/4333796/
	```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191226133000858.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

完成后查看：

```powershell
cd /usr/local/Caskroom/android-sdk/4333796/ && ls
# 将会看到  tools、platform-tools、build-tools 三个文件夹
```
然后在在 `~/.bash_profile` 中配置`ANDROID_HOME`，终端输入： `vim ~/.bash_profile`，然后点击`i`键进入编辑模式，添加如下：

```powershell
export ANDROID_HOME=/usr/local/Caskroom/android-sdk/4333796
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools
```
然后运行：

```powershell
source ~/.bash_profile
```
再次执行 appium-doctor 检查 appium 环境，如下：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191226132909347.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

至此Android环境搭建完成了！！！真机可直接运行。
如果需要使用 android 模拟器，则需要第`XIV`步安装模拟器

#### XV 安装 emulator
首先需要下载镜像文件：

```powershell
# 查看所有可安装的组件
sdkmanager --list --verbose
# 更新组件
sdkmanager --update
# 安装
sdkmanager --install "system-images;android-28;google_apis;x86"
```

然后下载硬件加速器：

```powershell
sdkmanager --install "extras;intel;Hardware_Accelerated_Execution_Manager"
```
下一步创建模拟器：
`avdmanager` 详细介绍参考：[这里](https://developer.android.com/studio/command-line/avdmanager)

```powershell
avdmanager create avd -n test -k "system-images;android-28;google_apis;x86" -b x86 -c 100M -d 7 -f
```
最后运行模拟器：

```powershell
# test 为上边创建模拟器的名称（-n test）
emulator -avd  test
# 或者
emulator  @test
```

`Tips:`
> 启动时如果如报这个错误 `PANIC: Missing emulator engine program for 'x86' CPU.` 
> 则说明不能使用tools下的emulator，直接选择`/usr/local/Caskroom/android-sdk/4333796/emulator/emulator  @test` 启动尝试（尝试tools目录下的emulator和emulator目录下的哪个可以用哪个）

![在这里插入图片描述](https://img-blog.csdnimg.cn/2019122613261880.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)



## XVI 运行测试代码
此处只简单演示Python代码，详情参考：[这里](https://github.com/lucas234/appium-sample/tree/master/samples)
安装Python版的客户端：

```powershell
pip install appium-python-client
```

如果提示:`'pip: command not found'`，根据自己Python的版本运行命令（Python 3的话后边改为3）：

```powershell
brew install python@2
```
这样安装后运行python脚本需要使用：`python2  test_android.py`
运行`test_android.py`脚本（测试计算器）：
`真机还是模拟器自行切换注释代码！！！` [脚本下载](https://github.com/lucas234/appium-sample/blob/master/samples/python/test_android.py)
```python
# coding=utf-8
import unittest
from appium import webdriver
import time
import os


class AndroidSimpleTest(unittest.TestCase):
    def setUp(self):
        calculator_desired_caps = {
                'platformName': 'Android',
                'platformVersion': '9.0',
                # emulator
                'deviceName': 'emulator-5554',
                'appPackage': 'com.android.calculator2',
                'appActivity': 'com.android.calculator2.Calculator'
                # real device
                # 'deviceName': '520381b347dd148b',
                #'appPackage': 'com.sec.android.app.popupcalculator',
                #'appActivity': 'com.sec.android.app.popupcalculator.Calculator'
            }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', calculator_desired_caps)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_calculator(self):
        # real device
        #self.driver.find_element_by_accessibility_id("5").click()
        #self.driver.find_element_by_accessibility_id("Plus").click()
        #self.driver.find_element_by_accessibility_id("6").click()
        #self.driver.find_element_by_accessibility_id("Equal").click()
        #self.assertEqual(self.driver.find_element_by_id("txtCalc").text, "11")
        
        # ************
        # emulator
        self.driver.find_element_by_id("digit_5").click()
        self.driver.find_element_by_accessibility_id("plus").click()
        self.driver.find_element_by_id("digit_6").click()
        self.driver.find_element_by_accessibility_id("equals").click()
        self.assertEqual(self.driver.find_element_by_id("result").text, "11")
    
    @unittest.skip("skip")
    def test_something(self):
        pass

if __name__ == '__main__':
    unittest.main()

```
运行`test_ios.py`脚本（TestApp ）：
`应用于iOS模拟器！！！`  [TestApp 下载](https://github.com/lucas234/appium-sample/tree/master/apps)，[脚本下载](https://github.com/lucas234/appium-sample/blob/master/samples/python/iOS_sample_test.py)

```python
# coding=utf-8
import unittest
from appium import webdriver
import time
import os


class IosSimpleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
			  "platformName": "iOS",
			  "platformVersion": "12.1",
			  "deviceName": "iPad Pro",
			  "noReset": True,
			  "udid": "1A7A0E9D-98AE-4230-BC92-13F66901FCBA",
			  "orientation": "LANDSCAPE",
              "connectHardwareKeyboard":True,
			  "app": "/Users/XXXX/Downloads/TestApp.app"
			}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        input_field_A = self.driver.find_element_by_accessibility_id("IntegerA")
        input_field_A.clear()
        input_field_A.send_keys('8')
        input_field_B = self.driver.find_element_by_accessibility_id("IntegerB")
        input_field_B.clear()
        input_field_B.send_keys('6')
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click()
        answer = self.driver.find_element_by_accessibility_id("Answer")
        # self.assertEqual(answer.text, "14")
        self.assertEqual(answer.get_attribute("value"), "14")
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

```

iOS真机运行`test_ios_real.py`脚本：
脚本下载：[这里](https://github.com/lucas234/appium-sample/blob/master/samples/python/test_ios_real.py)，运行前确保`build`进程存在（或者直接运行前执行该命令）：

```powershell
cd /usr/local/lib/node_modules/appium/node_modules/appium-webdriveragent && xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination 'id=<udid>' test
```

```python
# coding=utf-8
import unittest
from appium import webdriver
import time
import os


class IosSimpleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
			  "platformName": "iOS",
			  "platformVersion": "11.2",
			  "deviceName": "Red’s iPad (2)",
			  "noReset": True,
			  "udid": "34861df52360e9243cfd7acb75801e1d58d6746f",
			  "orientation": "LANDSCAPE",
              "xcodeOrgId":"TEST INTERNATIONAL",
              "xcodeSigningId":"6387P24J3L",
			  "app": "/Users/XXXX/Desktop/test_ios/your.app"
			}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        input_field = self.driver.find_elements_by_ios_predicate('type == "XCUIElementTypeTextField"')[1]
        input_field.clear()
        time.sleep(2)
        input_field.send_keys('123456@test.com')
        password=self.driver.find_element_by_ios_predicate('type=="XCUIElementTypeSecureTextField"')
        password.clear()
        time.sleep(2)
        password.send_keys('123456@test.com')
        password.send_keys('\n')
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()


```

`Tips:`
```powershell
# 查看设备名（deviceName）
adb devices 
# 查看模拟器版本号（platformVersion）
adb shell getprop ro.build.version.release
# 查看appPackage、appActivity，运行命令时要确保打开了应用
# 例如：首先打开计算器，然后运行命令即可获取到（以 / 隔开，前边appPackage，后边 appActivity ）
# 如果是Windows，则把 grep 换成 findstr 
adb shell dumpsys window windows | grep "Current" 

# **********iOS************
# 安装 app
xcrun simctl install booted /Users/XXXX/Downloads/TestApp.app/
# 获取名称和udid（先启动模拟器，再运行命令）
xcrun simctl list | grep "(Booted)"
```
其他`adb`相关命令查看：[这里](https://blog.csdn.net/lb245557472/article/details/84068519)
其他`xcrun simctl`相关命令查看：[这里](https://blog.csdn.net/lb245557472/article/details/89493199)


## XVII 问题解决

> 问题一
>".android/repositories.cfg could not be loaded."
>这个问题是因为缺少`repositories.cfg`文件，直接运行 `mkdir -p .android && touch ~/.android/repositories.cfg` 即可

> 问题二
>"PANIC: can`t find avd system path"
>检查SDK目录是否有至less4个目录： emulator ， platforms ， platform-tools ， system-images
>缺少哪个安装哪个，安装方法：
> sdkmanager --install "emulator" 
>  sdkmanager --install "platforms;android-26"
>  sdkmanager --install "system-images;android-26;google_apis;x86"
>参考：[这里](https://androidcookie.com/panicavdpath-android_sdk_root.html)

> 问题三
> "library not found at ../emulator/lib64/qt/lib"
> 需要用tools下的emulator启动虚拟设备即可（尝试tools目录下的emulator和emulator目录下的哪个可以）


> 问题四
> "Original error: Could not find 'adb' in PATH"
> 这个问题首先确保ANDROID_HOME设置正确的话（使用server版启动没问题），启动 Appium 桌面版引起的，因为正常安装后启动需要在桌面版配置JAVA_HOME 和 ANDROID_HOME，配置后即可解决
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191226144802833.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMjQ1NTU3NDcy,size_16,color_FFFFFF,t_70)

> 问题五
> "Original error: Error Domain=com.facebook.WebDriverAgent Code=1 "Keyboard is not present" UserInfo={NSLocalizedDescription=Keyboard is not present}" mac 跑模拟器的时候，当定位到了输入框，但是无法输入内容，会报如上到错误，这是由于模拟器的键盘没有被弹出导致的
> 两种解决方案：
> 一是 直接在 desired_caps 中添加 `"connectHardwareKeyboard":True` 这一配置即可，配置参考：[这里](https://github.com/appium/appium-xcuitest-driver#desired-capabilities)
> 二是 打开APP，定位到输入框，然后在键盘上用快捷键 `command+shift+k`，看到键盘弹出即可


## 参考
- [iOS真机运行](http://appium.io/docs/en/drivers/ios-xcuitest-real-devices/)




