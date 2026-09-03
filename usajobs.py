'''
USAJOBS api key
'''

import os
from dotenv import load_dotenv
import requests

load_dotenv()

def search_jobs_usajobs(keyword: str, location:str) -> list:
    '''
    Helps find jobs in the USA
    keyword: a job title/skill that is used to find a certain job
    location: a place where the job is located
    '''
    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": os.getenv("USAJOBS_EMAIL"),
        "Authorization-Key": os.getenv("USAJOBS_API_KEY")

    }
    url = "https://data.usajobs.gov/api/search"
    parems = {
        "Keyword": keyword,
        "LocationName": location
    }
    request = requests.get(url, headers=headers, params=parems)
    data = request.json()
    jobs_lst = []
    for job in data["SearchResult"]["SearchResultItems"]:
        jobs_lst.append({
            "title":job["MatchedObjectDescriptor"]["PositionTitle"],
            "org":job["MatchedObjectDescriptor"]["OrganizationName"],
            "location": job["MatchedObjectDescriptor"]["PositionLocationDisplay"],
            "min_salary":job["MatchedObjectDescriptor"]["PositionRemuneration"][0]["MinimumRange"],
            "max_salary":job["MatchedObjectDescriptor"]["PositionRemuneration"][0]["MaximumRange"]

        })
    return jobs_lst
if __name__ == "__main__":
    print(search_jobs_usajobs("Python", "Washington, DC"))