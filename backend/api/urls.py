from django.urls import path

from . import views


app_name = "api"

urlpatterns = [
    path("get-current-usd/", views.get_current_usd),
]
