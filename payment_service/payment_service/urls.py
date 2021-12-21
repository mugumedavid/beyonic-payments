from django.urls import path, include
from rest_framework import routers

from payment_service.views.payment import PaymentViewSet

router = routers.DefaultRouter()
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('payment-service/', include(router.urls)),
]
