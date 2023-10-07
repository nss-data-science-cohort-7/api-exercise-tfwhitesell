import requests
import pandas as pd

def GetWbData(params, country = 'all', ind_type = 'indicator', indicator = ''):
    """
    Gets data from World Bank API.
    Define parameters as a dictionary variable.
        params = {
            'format': 'json',
            'per_page': 50,
            'date': '2000:2021'
        }
    Note: If you want to return a single year, just pass the year as an integer. To return a range, use the example here as a template.
    Default value for country is 'all'. To call a single country use its 2-letter code (eg US).
    To call multiple countries, use 2-letter codes concatenated together with a semicolon (eg US;CA).
    """
    lst = []
    endpoint = 'http://api.worldbank.org/v2/country/'
    country = country
    ind_type = ind_type
    indicator = indicator
    params = params
    url = f'{endpoint}/{country}/{ind_type}/{indicator}/'

    # get number of pages
    res = requests.get(url, params).json()
    pages = res[0]['pages']

    for page in range(1, pages + 1):
        params['page'] = page
        res = requests.get(url, params).json()
        lst.extend(res[1])
    
    df = pd.json_normalize(lst)

    return df
