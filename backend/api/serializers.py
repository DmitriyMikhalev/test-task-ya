from django.conf import settings
from rest_framework import serializers

from . import models


class BaseCurrencyRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CurrencyRequest
        fields = (
            "created_at",
            "origin_currency",
            "target_currency",
            "rate"
        )


class CurrencyRequestSerializerChild(BaseCurrencyRequestSerializer):
    class Meta(BaseCurrencyRequestSerializer.Meta):
        pass


class CurrencyRequestSerializerParent(BaseCurrencyRequestSerializer):
    recent_requests = serializers.SerializerMethodField()

    class Meta(BaseCurrencyRequestSerializer.Meta):
        fields = (
            "recent_requests",
            *BaseCurrencyRequestSerializer.Meta.fields
        )

    def get_recent_requests(self, obj):
        childs = self.Meta.model.objects.all()[:settings.RECENT_REQUESTS_MAX_COUNT]

        return CurrencyRequestSerializerChild(instance=childs, many=True).data
