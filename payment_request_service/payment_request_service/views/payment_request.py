from rest_framework import viewsets
from rest_framework import permissions

from models.models import PaymentRequest
from payment_request_service.serializers.payment_request import PaymentRequestSerializer


class PaymentRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for creating and editing payment requests.
    """
    queryset = PaymentRequest.objects.all().order_by('-date')
    serializer_class = PaymentRequestSerializer
    # permission_classes = [permissions.IsAuthenticated]
