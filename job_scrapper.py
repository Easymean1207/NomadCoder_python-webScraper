from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't request website")
    exit(1)
else:
    # print(response.text)  # show html code of website included in response
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")  # use keyword Arguments

""" using try-catch(except) """
# try:
#     response = get(f"{base_url}{search_term}")
#     response.raise_for_status()  # Check if there was an HTTP error
#     print(response.text)  # Show HTML code of website included in the response
# except Exception as e:
#     print("Can't request website:", e)
