from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .models import PaymentScheduler
from .serializers import PaymentSchedulerSerializer


class PaymentSchedulerViewSet(ViewSet):
    def list(self, request):
        payment_scheduler = PaymentScheduler.objects.all()
        serializer = PaymentSchedulerSerializer(payment_scheduler, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PaymentSchedulerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        payment_scheduler = get_object_or_404(PaymentScheduler, pk=pk)
        serializer = PaymentSchedulerSerializer(payment_scheduler)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        payment_scheduler = get_object_or_404(PaymentScheduler, pk=pk)
        payment_scheduler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class PaymentSchedulerView(APIView):
#     def get(self, request):
#         payment_scheduler = PaymentScheduler.objects.all()
#         serializer = PaymentSchedulerSerializer(payment_scheduler, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = PaymentSchedulerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class PaymentSchedulerViewUseId(APIView):
#     def get(self, request, pk):
#         payment_scheduler = get_object_or_404(PaymentScheduler, pk=pk)
#         serializer = PaymentSchedulerSerializer(payment_scheduler)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def delete(self, request, pk):
#         payment_scheduler = get_object_or_404(PaymentScheduler, pk=pk)
#         payment_scheduler.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
