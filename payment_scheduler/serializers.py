from rest_framework import serializers
from .models import PaymentScheduler


class PaymentSchedulerSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
    )

    class Meta:
        model = PaymentScheduler
        fields = "__all__"

    def check_exists(self, data):
        """
        Verifica se já existe um agendamento com a mesma combinação de campos.
        """
        if PaymentScheduler.objects.filter(
            data_pagamento=data.get("data_pagamento"),
            agencia=data.get("agencia"),
            conta=data.get("conta"),
            valor_pagamento=data.get("valor_pagamento"),
            permite_recorrencia=data.get("permite_recorrencia"),
            quantidade_recorrencia=data.get("quantidade_recorrencia"),
            intervalo_recorrencia=data.get("intervalo_recorrencia"),
            status_recorrencia=data.get("status_recorrencia"),
        ).exists():
            raise serializers.ValidationError(
                {
                    "non_field_errors": [
                        "Já existe um agendamento com esta combinação de campos."
                    ]
                }
            )
        return data

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
