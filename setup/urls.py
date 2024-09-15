from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/agendamentos/",
        include("payment_scheduler.urls", namespace="payment_scheduler"),
    ),
]
