import requests


def make_api_request(lat, lon):
    """ Make an API request to retrieve weather data based on latitude and longitude."""
    base_url = 'http://api.weatherbit.io/v2.0/current'
    params = {'key': 'enter_your_key', 'lat': lat, 'lon': lon}
    weather_data = {}
    try:
        response = requests.get(url=base_url, params=params)
        response.raise_for_status()
        weather_data = response.json().get('data')
    except Exception as error:
        print(f'Error: {error}')
    return weather_data
