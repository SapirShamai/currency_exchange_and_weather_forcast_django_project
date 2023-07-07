from django.shortcuts import render
from .froms.exchange_form import ExchangeForm
from .api_requests import make_api_request


def exchange(request):
    """View function to handle the currency exchange page"""
    template = 'currency_exchange/exchange.html'
    form = ExchangeForm()
    calculated_result = None
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            base_currency = request.POST.get('base_currency')
            conversion_currency = request.POST.get('conversion_currency')
            amount = float(request.POST.get('amount'))
            base_currency_result = make_api_request(base_currency)
            calculated_result = amount * base_currency_result.get(conversion_currency)
    return render(request, template, {'form': form, 'result': calculated_result})
