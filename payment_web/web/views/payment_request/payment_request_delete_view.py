import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.conf import settings

from models.models import Currency
from web.forms.payment_request_form import PaymentRequestForm


class PaymentRequestDeleteView(LoginRequiredMixin, FormView):
    template_name = 'payment_requests/paymentrequest_delete_form.html'
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
        self.delete_request(self.kwargs['id'])
        return HttpResponseRedirect(self.get_success_url())

    def get_request(self, request_id: int):
        return requests.get(self.requests_url + '%d?format=json' % request_id).json()

    def delete_request(self, pk):
        response = requests.delete(self.requests_url + '%d/' % pk)
        return response
