# coding=utf-8
# auther：Liul5
# date：2019/6/25 9:04
# tools：PyCharm
# Python：2.7.15
from appium import webdriver
import time


# 切换webview
mobile_desired_caps = {
    'platformName': 'Android',
    'platformVersion': '7.0',
    'deviceName': '520381b347dd148b',
    "app": r"C:\work\coding\RedAppUIAutomation\src\test\resources\app\android3.11Sprint3.apk",

    # 指定Chromedriver地址，
    "chromedriverExecutableDir": r"C:\Users\liul5\Downloads\chromedriver_win32",
    # "chromedriverExecutable": r"C:\Users\liul5\Downloads\chromedriver_win32\chromedriver.exe",
    # 声明中文
    "unicodeKeyboard": 'True',
    # 声明中文，否则不支持中文
    "resetKeyboard": 'True',
    # 执行时不重新安装包
    'noReset': 'True',
    'automationName': 'uiautomator2',
    'appPackage': 'au.com.lexisnexis.lexisred.preview',
    'appActivity': 'md58792837710833813faed441d566ae093.NativeTourActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', mobile_desired_caps)
driver.find_elements_by_id("au.com.lexisnexis.lexisred.preview:id/flBackground")[2].click()
driver.find_element_by_android_uiautomator("new UiSelector().text(\"Lexis Red Digital Library\")").click()
# switch to webview
webview = driver.contexts[-1]
driver.switch_to.context(webview)

print("###########################################")
print(driver.contexts)
# [u'NATIVE_APP', u'WEBVIEW_xxxxxxxxx']
# do some webby stuff
print(driver.find_element_by_id("btnLogoutConfirmation").is_displayed())
driver.find_element_by_id("btnLogoutConfirmation").click()

# switch back to native view
driver.switch_to.context(driver.contexts[0])









# _*_ coding=utf-8 _*_
import os
import re
import yaml
from appium_study import current_dir
from appium import webdriver
conf_path = os.path.join(current_dir, "environments")
flag = True


def get_devices_name():
    devices = os.popen("adb devices").read().split()[-2]
    devices_name = devices if devices != "devices" else False
    if flag and devices_name:
        print("get the devices name successfull, devices name is %s" % devices_name)
    if not devices_name:
        print ("fail to get the devices name, please check the environment!")
    return devices_name


def get_app_path(apk_type="android"):
    if apk_type.lower() == "ios":
        apk_path = os.path.join(current_dir, r"package\ios")
    elif apk_type.lower() == "android":
        apk_path = os.path.join(current_dir, r"package\android")
    else:
        print "only support ios or android"
    if os.listdir(apk_path):
        all_apk_path = os.path.join(apk_path, os.listdir(apk_path)[0])
        if flag:
            print ("the apk path is: %s" % all_apk_path)
        return all_apk_path
    else:
        if flag:
            print ("the apk is not exist, please have a check!")
        return False


def get_app_info():
    path = get_app_path()
    command = "aapt dump badging " + path + " | findstr "
    pattern = re.compile(r"name='(.*?)'")
    app_package = pattern.findall(os.popen(command+"package").read())[0]
    app_activity = pattern.findall(os.popen(command+"launchable-activity").read())[0]
    if flag:
        print("get the app info successfull, app_package, app_activity is: %s, %s" % (app_package,app_activity))
    return app_package, app_activity


def create_driver(conf_name=None):
    actual_conf = conf_name or 'android'
    with open(os.path.join(conf_path, actual_conf)) as f:
        conf = yaml.load(f)
    app_package, app_activity = get_app_info()
    app = get_app_path()
    device_name = get_devices_name()
    desired_caps = conf.get("desired_caps")
    url = conf.get("command_executor")
    if device_name and app_package and app_activity:
        desired_caps.update({'app': app, 'deviceName': device_name,
                             'appPackage': app_package, 'appActivity': app_activity})
        driver = webdriver.Remote(url, desired_caps)
        if flag:
            print("driver start successfully!")
        return driver
















