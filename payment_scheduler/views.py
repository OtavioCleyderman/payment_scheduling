from rest_framework.viewsets import ModelViewSet


from .models import PaymentScheduler
from .serializers import PaymentSchedulerSerializer


class PaymentSchedulerViewSet(ModelViewSet):
    serializer_class = PaymentSchedulerSerializer
    queryset = PaymentScheduler.objects.all()
