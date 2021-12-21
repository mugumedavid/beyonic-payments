import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from models.models import PaymentRequest
from web.forms.payment_form import PaymentForm


class PaymentUpdateView(LoginRequiredMixin, FormView):
    template_name = 'payments/payment_form.html'
    form_class = PaymentForm
    success_url = '/beyonic-payments/payments/'
    payments_service_url = settings.PAYMENT_SERVICE_URL

    def get(self, request, *args, **kwargs):
        payment = requests.get(self.payments_service_url + '%d?format=json' % kwargs['id']).json()
        payment['payment_request'] = PaymentRequest.objects.get(transaction_id=payment.get('payment_request'))
        form = PaymentForm(data=payment)
        context = {'object': payment, 'form': form}
        return self.render_to_response(context)

    def form_valid(self, form):
        payment_request = self.get_request(self.kwargs['id'])
        payment_request['date'] = f'{form.cleaned_data["date"]:%Y-%m-%dT%H:%M:%S%z}'
        self.save_request(self.kwargs['id'], payment_request)

        return HttpResponseRedirect(self.get_success_url())

    def get_request(self, request_id: int):
        return requests.get(self.payments_service_url + '%d?format=json' % request_id).json()

    def save_request(self, pk, object):
        response = requests.put(
            self.payments_service_url + '%d/' % pk,
            object).json()
        return response