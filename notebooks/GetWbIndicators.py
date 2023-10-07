import requests
import pandas as pd

def GetWbIndicators(params, country = '', ind_type = '', indicator = ''):
    lst = []
    endpoint = 'http://api.worldbank.org/v2/indicator/'
    country = country
    ind_type = type
    indicator = indicator
    params = params
    url = f'{endpoint}/{country}/{ind_type}/{indicator}/'

    # get number of pages
    res = requests.get(url, params).json()
    pages = res[0]['pages']

    for page in range(1, pages + 1):
        params['page'] = page
        res = requests.get(url, params).json()
        lst.append(res[1])
    
    df = pd.json_normalize([r for d in lst for r in d])

    return df