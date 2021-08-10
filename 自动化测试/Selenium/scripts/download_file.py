# _*_ coding=utf-8 _*_
from selenium import webdriver
from time import sleep

# 火狐
# profile = webdriver.FirefoxProfile()
# profile.set_preference("browser.download.dir", "C:\\Users\\saas\\Desktop\\test_download")
# profile.set_preference('browser.download.manager.showWhenStarting', False)  # 在开始下载时是否显示下载管理器
# profile.set_preference("browser.download.folderList", 2)  # browser.download.folderList 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
# profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream, application/vnd.ms-excel, text/csv, application/zip")
# driver = webdriver.Firefox(firefox_profile=profile)
# driver.get('http://sahitest.com/demo/saveAs.htm')
# driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
# sleep(3)
# driver.quit()


# Chrome
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,  # 设置为 0 禁止弹出窗口
         'download.default_directory': 'C:\\Users\\saas\\Desktop\\test_download'}  # 设置下载路径
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit()

