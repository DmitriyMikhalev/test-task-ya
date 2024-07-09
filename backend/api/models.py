from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyRequest(models.Model):
    created_at = models.DateTimeField(
        verbose_name=_("Дата выполнения запроса"),
        auto_now_add=True
    )
    origin_currency = models.CharField(
        verbose_name=_("Наименование исходной валюты"),
        max_length=3,
        default="USD"
    )
    target_currency = models.CharField(
        verbose_name=_("Наименование результирующей валюты"),
        max_length=3,
        default="RUB"
    )
    rate = models.FloatField(
        verbose_name=_("Курс (по данным ЦБ РФ)"),
        null=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Запрос валютного курса")
        verbose_name_plural = _("Запросы валютного курса")

    def __str__(self) -> str:
        return f"1 {self.origin_currency} —> {self.rate} {self.target_currency}"
