from django.db import models
from models.models.base_model import BaseModel


class Currency(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    short_name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=255, null=False, blank=False)

    class Meta(object):
        verbose_name_plural = "Currencies"

    def __str__(self):
        return "%s" % (self.short_name,)
