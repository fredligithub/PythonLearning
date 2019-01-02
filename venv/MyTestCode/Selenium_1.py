# 安装： pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# WebDriver is an open source tool for automated testing of webapps across many browsers. 
# It provides capabilities for navigating to web pages, 
# user input, JavaScript execution, and more. 
browser = webdriver.Chrome('E:/Tools/Extensions/chromedriver_win32/chromedriver.exe')

# Open Web Page
browser.get('http://www.baidu.com/')
# Sleep 5 seconds till the web page is opened
time.sleep(5)

# 找到百度搜索框
input = browser.find_element_by_id('kw')
# 输入关键字
input.send_keys('Python')
# 回车
input.send_keys(Keys.ENTER)

time.sleep(3)
# 点击页面顶部 “贴吧”
browser.find_element_by_link_text('贴吧').click()