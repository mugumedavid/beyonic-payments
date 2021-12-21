from django.contrib import admin

from models.admin.base import BaseAdmin
from models.models import Currency

admin.site.register(Currency, BaseAdmin)
