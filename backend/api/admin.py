from django.contrib import admin

from . import models


@admin.register(models.CurrencyRequest)
class CurrencyRequestModel(admin.ModelAdmin):
    list_display = ("created_at", "rate", "origin_currency", "target_currency")
    date_hierarchy = "created_at"

    def has_change_permission(self, request, obj=None) -> bool:
        return False
