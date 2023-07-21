# check website is avaiable

import ctypes
import requests

websites = (
    "google.com",
    "https://facebook.com",
    "github.com",
    "naver.com",
    "https://twitter.com",
    "https://httpstat.us/501",
    "https://httpstat.us/404",
    "https://httpstat.us/307",
    "https://httpstat.us/101",
)
websites_list = list(websites)

results = {}

for index, item in enumerate(websites_list):
    if not item.startswith("https://"):
        websites_list[index] = f"https://{item}"
    response = requests.get(websites_list[index])

    if response.status_code >= 500:
        results[websites_list[index]] = "Server error"
    elif response.status_code >= 400:
        results[websites_list[index]] = "Client error"
    elif response.status_code >= 300:
        results[websites_list[index]] = "Redirection message"
    elif response.status_code >= 200:
        results[websites_list[index]] = "Successful response"
    elif response.status_code >= 100:
        results[websites_list[index]] = "Information response"
    else:
        results[websites_list[index]] = "Not supported response"


websites = tuple(websites_list)
# print(websites)
print(results)
