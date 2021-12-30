import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic


class PaymentRequestListView(LoginRequiredMixin, generic.TemplateView):
    context_object_name = 'requests'
    template_name = 'payment_requests/requests_list.html'
    fields = ('transaction_id', 'amount', 'date', 'currency')
    requests_url = settings.REQUEST_SERVICE_URL

    def get(self, request, *args, **kwargs):
        payment_requests = requests.get(self.requests_url + '?format=json')
        payment_requests_json = {}
        if payment_requests:
            payment_requests_json = payment_requests.json()
        context = {'requests': payment_requests_json}
        return render(request, "payment_requests/requests_list.html", context=context)
