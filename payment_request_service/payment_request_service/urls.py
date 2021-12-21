from django.urls import path, include
from rest_framework import routers
from payment_request_service.views import PaymentRequestViewSet

router = routers.DefaultRouter()
router.register(r'payment-request', PaymentRequestViewSet)

urlpatterns = [
    path('payment-request-service/', include(router.urls)),
]
