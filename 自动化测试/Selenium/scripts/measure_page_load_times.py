# auther：Liul8
# date：2020/5/11 16:18
# tools：PyCharm
# Python：3.7.7
# reference:  https://www.lambdatest.com/blog/how-to-measure-page-load-times-with-selenium/
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


hyperlink = "http://lambdatest.com"

driver = webdriver.Chrome(r"C:\diy\old coding\test\locust demo\appium-sample\drivers\chromedriver.exe")
driver.get(hyperlink)

# # first
# ''' Use Navigation Timing  API to calculate the timings that matter the most '''
# navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
# responseStart = driver.execute_script("return window.performance.timing.responseStart")
# domComplete = driver.execute_script("return window.performance.timing.domComplete")
# ''' Calculate the performance'''
# backendPerformance_calc = responseStart - navigationStart
# frontendPerformance_calc = domComplete - responseStart
# print("Back End: %s" % backendPerformance_calc)
# print("Front End: %s" % frontendPerformance_calc)
# driver.quit()


# # second
# timeout = 15
#
# ''''' Test case 1 - The required div-id is not present on the web-page '''''
# # while True:
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'owl-example-1'))
#     WebDriverWait(driver, timeout).until(element_present)
#     print("1 - Element is present on the page")
# #        break
# except TimeoutException as ex:
#     print("1 - Timed out waiting for page to load " + str(ex))
# #        break
#
# ''''' Test case 2 - The required div-id is not present on the web-page '''''
# # while True:
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'owl-example'))
#     WebDriverWait(driver, timeout).until(element_present)
#     print("2 - Element is present on the page")
# #        break
# except TimeoutException as ex:
#     print("2 - Timed out waiting for page to load " + str(ex))
# #        break
#
# ''' Free up the resources'''
# driver.close()
# driver.quit()


''' Import the 'modules' that are required for execution '''
''' In this example, we make use of pytest framework along with Selenium '''
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    staleness_of


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.lambdatest.com/")
        print(self.driver.title)
        sleep(5)

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        # Search for the div-id owl-example
        old_page = self.driver.find_element_by_id('owl-example')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(old_page)
        )

    def test_click_operation(self):
        # Wait for a timeout duration of 10 seconds, after which we perform a CLICK operation
        with self.wait_for_page_load(timeout=10):
            self.driver.find_element_by_link_text('FREE SIGN UP').click()
            print(self.driver.execute_script("return document.readyState"))