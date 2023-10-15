from requests import get
from bs4 import BeautifulSoup


def extractWwrJobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request website")
        exit(1)
    else:
        results = []
        # print(response.text)  # show html code of website included in response
        soup = BeautifulSoup(
            response.text, "html.parser"
        )  # BeautifulSoup transform everything to python datastructure
        jobs = soup.find_all("section", class_="jobs")  # use keyword Argument

        for job_section in jobs:
            job_posts = job_section.find_all("li")
            job_posts.pop(-1)  # remove view-all(last index)

            for post in job_posts:
                anchors = post.find_all("a")
                anchor = anchors[1]  # get second anchor

                link = anchor["href"]
                company, kind, region = anchor.find_all(
                    "span", class_="company"
                )  # another way to assign value if we know length of list
                title = anchor.find("span", class_="title")

                job_data = {
                    "link": f"https//weworkremotely.com{link}",
                    "company": company.string,
                    "location": region.string,
                    "position": title.string,
                }
                results.append(job_data)

        return results
