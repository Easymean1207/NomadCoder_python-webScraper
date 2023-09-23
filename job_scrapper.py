from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwwr_jobs
from selenium import webdriver

# indeed.com은 bot으로 감지하여 anti-bot 사이트를 띄움 -> selenium을 이용한 브라우저 자동화가 필요
base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

browser = webdriver.Chrome()
browser.get(base_url + search_term)
# print(browser.page_source)

results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh")  # use find method
jobs = job_list.find_all("li", recursive=False)  # only search direct li

for job in jobs:
    zone = job.find("div", class_="mozaic-zone")
    if zone == None:  # None is python's Null type
        anchor = job.select_one("h2 a")  # use select method (using css selector)
        if anchor != None:
            # data extraction from jobTitle class
            title = anchor["aria-label"]
            link = anchor["href"]
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")

            # input extracted data into job_data
            job_data = {
                "link": f"https://kr.indeed.com{link}",
                "company": company.string,
                "location": location.string,
                "position": title,  # position is aria-label
            }
            results.append(job_data)

for result in results:
    print(result, "\n///////\n")

while True:
    pass
