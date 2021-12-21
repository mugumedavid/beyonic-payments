from django.contrib.auth.models import User
from rest_framework import serializers

from models.models import PaymentRequest, Payment


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%d")
    payment_request = serializers.SlugRelatedField(many=False, queryset=PaymentRequest.objects.all(),
                                                   slug_field='transaction_id', read_only=False)
    approved_by = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=User.objects.all()
    )

    class Meta:
        model = Payment
        fields = ['date', 'payment_request', 'approved_by', 'id']
