import requests

print("requests library version: ",requests.__version__)

print("GET the Google homepage:\n",requests.get("https://www.google.com/"))