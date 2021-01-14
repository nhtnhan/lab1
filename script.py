import requests

print("requests library version: ",requests.__version__)

print("GET the Python source code:\n",requests.get("https://raw.githubusercontent.com/nhtnhan/lab1/master/script.py"))