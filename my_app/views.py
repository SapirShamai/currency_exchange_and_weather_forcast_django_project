from django.urls import reverse
from django.http import HttpResponse


def home(request):
    response = ['<h1>WELCOME</h1>',
                '<a href="', reverse('currency_exchange:home'), '"><button>Currency Exchange</button></a>',
                '<br>', '<br>'
                '<a href="', reverse('weather_forcast:home'), '"><button>Weather Forcast</button></a>'
                ]
    return HttpResponse(''.join(response))
