from django import forms
from django.forms import widgets

from models.models import Currency


class PaymentRequestForm(forms.Form):

    transaction_id = forms.CharField(max_length=10, required=True)
    amount = forms.FloatField(required=True)
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(), required=True)
    date = forms.DateField(required=True, widget=widgets.DateInput(attrs={'type': 'date'}))
    id = forms.HiddenInput()
