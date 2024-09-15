from django.urls import path
from .views import PaymentSchedulerViewSet
from rest_framework import routers

app_name = "payment_scheduler"
router = routers.SimpleRouter()
router.register(r"", PaymentSchedulerViewSet, basename="payment_scheduler")
urlpatterns = router.urls
