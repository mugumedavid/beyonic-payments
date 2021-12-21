from django.conf.urls import url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import path

from web.views.payment.payment_list import PaymentListView

from web.views.payment.payment_form_view import PaymentFormView
from web.views.payment.payment_update_view import PaymentUpdateView
from web.views.payment_request.payment_request_delete_view import PaymentRequestDeleteView
from web.views.payment_request.payment_request_list import PaymentRequestListView
from web.views.payment_request.payment_request_form_view import PaymentRequestFormView
from web.views.payment_request.payment_request_update_view import PaymentRequestUpdateView

urlpatterns = [
    url(r'$', LoginView.as_view(),
        {'template_name': 'login.html', 'authentication_form': AuthenticationForm}, name='login'),
    url(r'beyonic-payments/requests/$', PaymentRequestListView.as_view(), name='requests'),
    path('beyonic-payments/requests/delete/<int:id>', PaymentRequestDeleteView.as_view(), name='delete-request'),
    path('beyonic-payments/requests/<int:id>', PaymentRequestUpdateView.as_view(), name='update-request'),
    path('beyonic-payments/requests/add/', PaymentRequestFormView.as_view(), name='new-request'),
    url(r'beyonic-payments/payments/$', PaymentListView.as_view(), name='payments'),
    # path('beyonic-payments/payments/<int:pk>', PaymentDeleteView.as_view(), name='delete-payment'),
    path('beyonic-payments/payments/<int:id>', PaymentUpdateView.as_view(), name='update-payment'),
    path('beyonic-payments/payments/add/', PaymentFormView.as_view(), name='new-payment'),
]
