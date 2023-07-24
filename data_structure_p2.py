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
    "https://httpstat.us/306",
    "https://httpstat.us/101",
)

websites_list = list(websites)

results = {}

""" enumerate: 인덱스와 요소로 이루어진 tuple을 반환 -> 값을 변형하고 싶으면 list의 형태로 바꿔야 함 ★★★★★"""
# for index, item in enumerate(websites_list):

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = requests.get(website)

    if response.status_code >= 500:
        results[website] = "5xx / Server error"
    elif response.status_code >= 400:
        results[website] = "4xx / Client error"
    elif response.status_code >= 300:
        results[website] = "3xx / Redirection message"
    elif response.status_code >= 200:
        results[website] = "2xx / Successful response"
    elif response.status_code >= 100:
        results[website] = "1xx / Information response"
    else:
        results[website] = "Not supported response"

# websites = tuple(websites_list)
# print(websites)

for website_key in results:
    print(website_key, "->", results[website_key])
