"""
Check the current status of any website by this automation script that uses the Urllib3 module that sends the HTTP request to the website and in response we can get the current web status.
"""

# Web Status Checker
# pip install urllib3
import urllib3


import time
web = "http://www.google.com"
http = urllib3.PoolManager()
response = http.request('GET', web)
if response.status == 200:
    print("Web is online")
else:
    print("Web is offline")