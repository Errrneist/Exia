# Hongjun Wu
# 20180204
# This is a program to test web driver.

from selenium import webdriver
import urllib3
import urllib
import re

# This driver will call weibo and then call zhihu.
driver = webdriver.Chrome()
# driver.get('https://ucharm.hfs.washington.edu/ucharm/SelectRoom.asp?Function=1060&fld38517=10673')
url = 'https://ucharm.hfs.washington.edu/ucharm/SelectRoomResults.asp'
isLogIn = False
driver.get('https://ucharm.hfs.washington.edu/ucharm/SelectRoomResults.asp')

html_content = urllib.urlopen(url).read()

hasSpot = False

while not hasSpot:
    html_content = urllib.urlopen('https://ucharm.hfs.washington.edu/ucharm/SelectRoomResults.asp').read()
    matches = re.findall('There are no rooms available', html_content)
    if len(matches) != 0:
        driver.get('https://ucharm.hfs.washington.edu/ucharm/SelectRoomResults.asp')




