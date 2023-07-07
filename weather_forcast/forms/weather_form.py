from django import forms


class WeatherForm(forms.Form):
    latitude = forms.DecimalField()
    longitude = forms.DecimalField()