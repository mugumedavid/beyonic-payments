from django import forms
from django.forms import widgets

from models.models import PaymentRequest


class PaymentForm(forms.Form):

    payment_request = forms.ModelChoiceField(queryset=PaymentRequest.objects.all(), required=True)
    date = forms.DateField(required=True, widget=widgets.DateInput(attrs={'type': 'date'}))
    approved_by = forms.HiddenInput()
