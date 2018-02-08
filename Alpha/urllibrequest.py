# Hongjun Wu
# 20180204
# This program is a test file for urllib.

import urllib.request

response = urllib.request.urlopen('http://www.spacex.com')

# Print the entire source of the website.
print("I am about to print the contents of the website:")
print()
print(response.read().decode('utf-8'))
