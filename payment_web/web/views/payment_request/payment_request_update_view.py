import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.conf import settings

from models.models import Currency
from web.forms.payment_request_form import PaymentRequestForm


class PaymentRequestUpdateView(LoginRequiredMixin, FormView):
    template_name = 'payment_requests/paymentrequest_form.html'
    form_class = PaymentRequestForm
    success_url = '/beyonic-payments/requests/'
    requests_url = settings.REQUEST_SERVICE_URL

    def get(self, request, *args, **kwargs):
        payment_request = requests.get(
            self.requests_url + '%d?format=json' % kwargs['id']).json()
        payment_request['currency'] = Currency.objects.get(short_name=payment_request.get('currency'))
        form = PaymentRequestForm(data=payment_request)
        context = {'object': payment_request, 'form': form}
        return self.render_to_response(context)

    def form_valid(self, form):
        payment_request = self.get_request(self.kwargs['id'])
        payment_request['currency'] = Currency.objects.get(short_name=payment_request.get('currency')).short_name
        payment_request['transaction_id'] = form.cleaned_data['transaction_id']
        payment_request['amount'] = form.cleaned_data['amount']
        payment_request['date'] = f'{form.cleaned_data["date"]:%Y-%m-%dT%H:%M:%S%z}'
        self.save_request(self.kwargs['id'], payment_request)

        return HttpResponseRedirect(self.get_success_url())

    def get_request(self, request_id: int):
        return requests.get(self.requests_url + '%d?format=json' % request_id).json()

    def save_request(self, pk, object):
        response = requests.put(
            self.requests_url + '%d/' % pk,
            object).json()
        return response
