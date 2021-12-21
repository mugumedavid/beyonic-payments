from rest_framework import serializers

from models.models import PaymentRequest, Currency


class PaymentRequestSerializer(serializers.HyperlinkedModelSerializer):
    currency = serializers.SlugRelatedField(many=False, queryset=Currency.objects.all(),
                                                     slug_field='short_name', read_only=False)
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = PaymentRequest
        fields = ['amount', 'date', 'currency', 'transaction_id', 'id']
