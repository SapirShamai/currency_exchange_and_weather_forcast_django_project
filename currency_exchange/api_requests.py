import requests


def make_api_request(base_currency):
    """MAke an API request to retrieve conversion rates based on base_currency param"""
    params = {'apikey': 'enter_your_key', 'base_currency': base_currency}
    base_url = 'https://api.freecurrencyapi.com/v1/latest'
    result = {}
    try:
        response = requests.get(url=base_url, params=params)
        response.raise_for_status()
        result = response.json().get('data')
    except Exception as error:
        print(f'Error: {error}')
    return result


def get_all_currency_codes():
    """ getting a list with all the currency codes from the api
    used to create the currency code choices in form"""
    all_currencies = []
    json_result = make_api_request('USD')
    for i in json_result:
        all_currencies.append((i, i))
    return all_currencies
