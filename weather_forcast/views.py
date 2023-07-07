from django.shortcuts import render
from .forms.weather_form import WeatherForm
from .api_requests import make_api_request


def weather(request):
    """View function to handle the weather forecast page.
      Returns the rendered weather forecast page."""
    form = WeatherForm()
    template = 'weather_forcast/weather.html'
    result = None
    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            api_request = make_api_request(latitude, longitude)
            temp = api_request[0].get('app_temp')
            city = api_request[0].get('city_name')
            description = api_request[0].get('weather').get('description')
            result = [temp, city, description]
    return render(request, template, {'form': form, 'result': result})

