from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    readonly_fields = ('created_at', 'modified_on', 'created_by', 'modified_by')
    date_hierarchy = 'created_at'
