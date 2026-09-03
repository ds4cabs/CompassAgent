'''
O*NET API
'''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def search_onset_skill(skill: str) -> list:
    '''
    Helps in finding a specific occupation based on a certain skill/technology
    skill is for finding a certain occupation
    '''
    headers = {
        "X-Api-Key": os.getenv("ONET_API_KEY")
    }

    search_url = "https://api-v2.onetcenter.org/online/technology/examples/search"
    parms = {"keyword": skill}
    response_1 = requests.get(search_url, headers=headers, params=parms)
    data_1 = response_1.json()
    first_href = data_1["example"][0]["href"]
    response_2 = requests.get(first_href, headers=headers)
    data_2 = response_2.json()

    occupations = []

    for occ in data_2['occupation']:
        occupations.append({
            'title': occ["title"],
            'code': occ['code']
        })

    return occupations

if __name__ == "__main__":
    print(search_onset_skill("Python"))