from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import utils, serializers, models


@api_view(http_method_names=("GET",))
def get_current_usd(request):
    rate = utils.get_cbr_rate()
    serializer_class = serializers.CurrencyRequestSerializerParent

    if rate:
        instance = models.CurrencyRequest.objects.create(rate=rate)
    else:
        instance = models.CurrencyRequest.objects.first()

    return Response(data=serializer_class(instance=instance).data)
