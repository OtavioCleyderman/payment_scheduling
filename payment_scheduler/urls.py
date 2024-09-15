from django.urls import path
from .views import PaymentSchedulerView
from .views import PaymentSchedulerViewUseId

app_name = "payment_scheduler"
urlpatterns = [
    path("", PaymentSchedulerView.as_view(), name="payment_scheduler-list"),
    path(
        "<int:pk>/",
        PaymentSchedulerViewUseId.as_view(),
        name="payment_scheduler-details",
    ),
]
