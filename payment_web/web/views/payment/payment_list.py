import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from models.models import Payment


class PaymentListView(LoginRequiredMixin, generic.ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'payments/payments_list.html'
    fields = ('transaction_id', 'amount', 'date', 'currency')
    payments_service_url = settings.PAYMENT_SERVICE_URL

    def get(self, request, *args, **kwargs):
        payments = requests.get(self.payments_service_url + '?format=json')
        payment_json = {}
        if payments:
            payment_json = payments.json()
        context = {'payments': payment_json}
        return render(request, "payments/payments_list.html", context=context)
