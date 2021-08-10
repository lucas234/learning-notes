# coding=utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)

    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)


driver = Chrome(executable_path=r"C:\Users\liul5\Documents\test\after_Nov\driver\chromedriver.exe", )
ef_driver = EventFiringWebDriver(driver, MyListener())
ef_driver.get("http://zhihu.com")
# assert "TestArt" in ef_driver.title

ef_driver.close()
