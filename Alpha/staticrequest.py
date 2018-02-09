# Hongjun Wu
# 2018024
# Simple request that requests a website from Google
# and prints out the HTML source codes.

# Import statement
import requests

# Pre: Assign user agent
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}

# Assign the response to a variable named response.
response = requests.get('http://www.google.com', headers=headers)

# Post: print the text from the response.
print('This is the HTML source code:')
print(response.text)
print()

# Post: Print the response header.
print('This is the HTML response header:')
print(response.headers)
print()

# Post: Print status code.
print('This is the response code:')
print(response.status_code)
print()

# Get a Rembrandt icon from Google.
response = requests.get("https://lh3.googleusercontent.com/-tFrHVdnk0KQ"
                        "/AAAAAAAAAAI/AAAAAAAAAAA/ACSILjXB7PREzu493Bt66sdDnIwawt7lQw"
                        "/s64-c-mo/photo.jpg")

# Print binary code of the Rembrandt image
print(response.content)

# Save the image of Rembrandt
with open('./Rembrandt.jpg', 'wb') as f:
    f.write(response.content)
    f.close()

