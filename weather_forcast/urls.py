from django.urls import path
from .views import weather
app_name = 'weather_forcast'

urlpatterns = [
    path('', weather, name='home'),
    # path('test/', make_api_request, name='test')
]
