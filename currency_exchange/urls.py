from django.urls import path
from .views import exchange
app_name = 'currency_exchange'

urlpatterns = [
    path('', exchange, name='home'),
]
