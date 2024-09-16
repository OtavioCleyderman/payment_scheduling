from rest_framework import serializers
from .models import PaymentScheduler
from decimal import Decimal


class PaymentSchedulerSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.IntegerField(min_value=1)

    class Meta:
        model = PaymentScheduler
        fields = [
            "id",
            "data_pagamento",
            "permite_recorrencia",
            "quantidade_recorrencia",
            "intervalo_recorrencia",
            "status_recorrencia",
            "agencia",
            "conta",
            "valor_pagamento",
        ]

    def to_internal_value(self, data):
        if "valor_pagamento" in data and isinstance(
            data["valor_pagamento"], (float, Decimal)
        ):
            data["valor_pagamento"] = int(round(Decimal(data["valor_pagamento"]) * 100))
        return super().to_internal_value(data)

    # Caso optem por retornar como decimal também. Só descomentar o trecho abaixo
    # def to_representation(self, instance):
    #     valores_salvos = super().to_representation(instance)
    #     valores_salvos["valor_pagamento"] = float(instance.valor_pagamento) / 100
    #     return valores_salvos
