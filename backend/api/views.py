from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.conf import settings

from . import utils, serializers, models


@api_view(http_method_names=("GET",))
def get_current_usd(request):
    recent_request = models.CurrencyRequest.objects.first()
    serializer_class = serializers.CurrencyRequestSerializerParent

    if not recent_request:
        if rate := utils.get_cbr_rate():
            instance = models.CurrencyRequest.objects.create(rate=rate)
        else:
            return Response({"detail": _("Провайдер курса недоступен, сохраненные данные отсутствуют.")})
    else:
        if (now() - recent_request.created_at).seconds < settings.TIMEOUT_SECONDS:
            instance = recent_request
        else:
            instance = models.CurrencyRequest.objects.create(rate=utils.get_cbr_rate())

    return Response(data=serializer_class(instance=instance).data)
