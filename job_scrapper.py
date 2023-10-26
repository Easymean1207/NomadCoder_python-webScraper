import os
from extractors.indeed import extractIndeedJobs
from extractors.wwr import extractWwrJobs

keyword = input("what do you want to search? ")

indeed = extractIndeedJobs(keyword)
wwr = extractWwrJobs(keyword)

jobs = indeed + wwr

if os.path.exists(f"{keyword}.csv"):
    os.remove(f"{keyword}.csv")

try:
    with open(
        f"{keyword}.csv", "w", encoding="utf-8-sig"
    ) as file:  # .csv (comma seperated value) -> 액셀 테이블과 비슷함.
        file.write("Position, Company, Location, URL\n")

        for job in jobs:
            file.write(
                f"{job['position']}, {job['company']},{job['location']},{job['link']}\n"
            )

    file.close()

except Exception as e:
    print(f"예외가 발생하였습니다: {e}")
