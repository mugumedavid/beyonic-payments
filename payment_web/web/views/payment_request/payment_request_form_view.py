import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from web.forms.payment_request_form import PaymentRequestForm


class PaymentRequestFormView(LoginRequiredMixin, FormView):
    template_name = 'payment_requests/paymentrequest_form.html'
    form_class = PaymentRequestForm
    success_url = '/beyonic-payments/requests/'
    requests_url = settings.REQUEST_SERVICE_URL

    def form_valid(self, form):
        payment_request = {'currency': form.cleaned_data['currency'].short_name,
                           'transaction_id': form.cleaned_data['transaction_id'], 'amount': form.cleaned_data['amount'],
                           'date': f'{form.cleaned_data["date"]:%Y-%m-%dT%H:%M:%S%z}'}
        self.save_request(payment_request)

        return HttpResponseRedirect(self.get_success_url())

    def save_request(self, request):
        response = requests.post(self.requests_url, request)
        return response
