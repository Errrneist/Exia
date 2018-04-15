"""
Hongjun Wu
20180209
This program attempts to refresh learning catalytics.
"""
from selenium import webdriver
driver = webdriver.Chrome()
isRefresh = True
while isRefresh:
    driver.get('https://learningcatalytics.com/class_sessions/review')
