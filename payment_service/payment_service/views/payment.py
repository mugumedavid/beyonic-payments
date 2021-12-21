from rest_framework import viewsets
from rest_framework import permissions

from models.models import Payment
from payment_service.serializers.payment import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for approval and issuance of payments based on logged payment requests.
    """
    queryset = Payment.objects.all().order_by('-date')
    serializer_class = PaymentSerializer
    # permission_classes = [permissions.IsAuthenticated]
