'''
NIH RePORTER API KEY
'''

import requests

def find_pi_labs_nih(topic:str, limit: int = 10)-> list:

    '''
    Helps return Principal Investigators/Researchers as well as their Institutions/labs
    topic is the keyword the user uses for requesting a specific type of research field
    '''

    url = "https://api.reporter.nih.gov/v2/projects/search"
    body = {
        "criteria": {
            "advanced_text_search": {
                "operator": "and",
                "search_field": "all",
                "search_text": topic
            }
        },
        "limit": limit
    }
    response = requests.request("POST", url, json=body)
    data = response.json()
    labs = []
    for project in data["results"]:
        labs.append({
            "pi": project["contact_pi_name"],
            "org": project["organization"]["org_name"]

        })
    return labs
if __name__ == "__main__":
    print(find_pi_labs_nih("CRISPR"))