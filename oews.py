'''
BLS (Bureau of Labor Statistics) API Key
'''

import requests

def get_owes_salary(occupation_code: str) -> list:
        '''
        Helps find a specific occupation's wage/salary data
        occupation_code is a type of 6-digit number with no dash that's the same one in the SOC code
        '''
        series_id = f"OEUN0000000000000{occupation_code}13"
        url = f"https://api.bls.gov/publicAPI/v1/timeseries/data/{series_id}"
        response = requests.get(url)
        data = response.json()
        # your extraction logic goes here
        dat = data['Results']['series'][0]['data'][0]['value']
        return dat


if __name__ == "__main__":
        print(get_owes_salary("152011"))