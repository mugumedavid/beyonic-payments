from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_created_by",
                                   related_query_name="%(app_label)s_%(class)ss",
                                   on_delete=models.PROTECT)
    modified_by = models.ForeignKey(User, blank=True, null=True,
                                    related_name="%(app_label)s_%(class)s_modified_by",
                                    related_query_name="%(app_label)s_%(class)ss",
                                    on_delete=models.PROTECT)

    class Meta:
        abstract = True
