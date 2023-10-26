from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
browser = webdriver.Chrome(options=options)


def getPageCount(keyword):
    base_url = "https://kr.indeed.com/jobs"
    browser.get(f"{base_url}?q={keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")

    pagination = soup.find("nav", {"aria-label": "pagination"})
    pages = pagination.find_all("div", recursive=False)
    count = len(pages)

    # 화살표 체크 및 제거
    for page in pages:
        aria_label = page.get("aria-label")
        if aria_label in ["Previous Page", "Next Page"]:
            count = count - 1

    if count <= 0:
        return 1
    if count >= 5:
        return 5
    else:
        return count


def extractIndeedJobs(keyword):
    # indeed.com은 bot으로 감지하여 anti-bot 사이트를 띄움 -> selenium을 이용한 브라우저 자동화가 필요
    pages = getPageCount(keyword)
    print("Found", pages, "pages")
    results = []

    for page in range(pages):
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("requesting", final_url)

        browser = webdriver.Chrome()
        browser.get(final_url)

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="css-zu9cdh")  # use find method
        jobs = job_list.find_all("li", recursive=False)  # only search direct li

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:  # None is python's Null type
                anchor = job.select_one(
                    "h2 a"
                )  # use select method (using css selector)
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

                    # check that replace() is available
                    for each in job_data:
                        if job_data[each] != None:
                            job_data[each] = job_data[each].replace(",", " ")

                    results.append(job_data)

    return results
