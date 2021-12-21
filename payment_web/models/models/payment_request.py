from django.db import models
from models.models.base_model import BaseModel


class PaymentRequest(BaseModel):
    amount = models.FloatField(null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False, verbose_name='Issued on')
    currency = models.ForeignKey("Currency", null=False, blank=False, on_delete=models.PROTECT)
    transaction_id = models.CharField(max_length=10, blank=False, null=False, unique=True)

    def __str__(self):
        return "%s%s - TXN %s" % (self.currency.short_name, self.amount,
                                  self.transaction_id)
