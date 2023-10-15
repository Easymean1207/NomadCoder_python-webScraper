from extractors.indeed import extractIndeedJobs
from extractors.wwr import extractWwrJobs

keyword = input("what do you want to search?")

indeed = extractIndeedJobs(keyword)
wwr = extractWwrJobs(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
    print("//////\n//////")
