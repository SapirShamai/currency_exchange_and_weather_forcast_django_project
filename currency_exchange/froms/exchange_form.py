from django import forms
from ..api_requests import get_all_currency_codes


class ExchangeForm(forms.Form):
    base_currency = forms.ChoiceField(choices=get_all_currency_codes(), initial='EUR')
    conversion_currency = forms.ChoiceField(choices=get_all_currency_codes(), initial='USD')
    amount = forms.DecimalField()


