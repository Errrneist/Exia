# Hongjun Wu
# 20180204
# This program will attempt to get resource from Sina Weibo which is not static.

import requests
response = requests.get('http://m.weibo.com')
print(response.text)
print(response.status_code)