# Hongjun Wu
# 20180204
# This is a program to test web driver.

from selenium import webdriver

# This driver will call weibo and then call zhihu.
driver = webdriver.Chrome()
driver.get('http://m.weibo.com')
driver.get('http://zhihu.com')
driver.get('http://bilibili.com')
