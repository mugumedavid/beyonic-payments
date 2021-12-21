from django.contrib.auth.models import User
from django.db import models
from models.models.base_model import BaseModel


class Payment(BaseModel):
    date = models.DateTimeField(null=False, blank=False)
    payment_request = models.OneToOneField("PaymentRequest", null=False, blank=False, on_delete=models.PROTECT)
    approved_by = models.ForeignKey(User, blank=False, null=False,
                                    related_name="%(app_label)s_%(class)s_approved_by",
                                    related_query_name="%(app_label)s_%(class)ss",
                                    on_delete=models.PROTECT)

    def __str__(self):
        return "%s" % self.payment_request
