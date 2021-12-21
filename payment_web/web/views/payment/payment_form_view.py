import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView

from web.forms.payment_form import PaymentForm


class PaymentFormView(LoginRequiredMixin, FormView):
    template_name = 'payments/payment_form.html'
    form_class = PaymentForm
    success_url = '/beyonic-payments/payments/'
    payments_service_url = settings.PAYMENT_SERVICE_URL

    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.pk)
        payment = {'payment_request': form.cleaned_data['payment_request'].transaction_id,
                   'approved_by': user.id,
                   'date': f'{form.cleaned_data["date"]:%Y-%m-%dT%H:%M:%S%z}'}
        self.save_payment(payment)

        return HttpResponseRedirect(self.get_success_url())

    def save_payment(self, payment):
        response = requests.post(self.payments_service_url, payment)
        return response
