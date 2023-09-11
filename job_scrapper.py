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

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh")
jobs = job_list.find_all("li", recursive=False)  # only search direct li

for job in jobs:
    print(job)
    print("////////////")


while True:
    pass
