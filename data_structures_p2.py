""" program that check specific website is avaiable """

import requests

websites = (
    "google.com",
    "https://facebook.com",
    "github.com",
    "https://naver.com",
    "https://twitter.com",
    "https://httpstat.us/501",
    "https://httpstat.us/404",
    "https://httpstat.us/306",
    "https://httpstat.us/101",
)

# websites_list = list(websites)
results = {}

""" enumerate: 인덱스와 요소로 이루어진 tuple을 반환 -> 값을 변형하고 싶으면 list의 형태로 바꿔야 함 ★★★★★
ex: for index, item in enumerate(websites_list): """

for website in websites:
    # convert to a website format
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = requests.get(website)

    # evalute website's status based on response status code
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


# for key, value in results.items():
#     print("{} : {}".format(key, value))

for website in results:
    print(website, "->", results[website])
