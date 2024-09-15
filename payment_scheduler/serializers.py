from rest_framework import serializers
from .models import PaymentScheduler


class PaymentSchedulerSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = PaymentScheduler
        fields = "__all__"

    def to_internal_value(self, data):
        valores_recebidos = super().to_internal_value(data)
        if "valor_pagamento" in valores_recebidos:
            valores_recebidos["valor_pagamento"] = int(
                round(valores_recebidos["valor_pagamento"] * 100)
            )
        return valores_recebidos

    def to_representation(self, instance):
        valores_salvos = super().to_representation(instance)
        valores_salvos["valor_pagamento"] = float(instance.valor_pagamento) / 100
        return valores_salvos
