from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime


def date_validate(value):
    data_atual = datetime.now()
    data_atual_formatada = data_atual.date()
    if value <= data_atual_formatada:
        raise ValidationError("Para agendamento, escolha uma data futura.")


class PaymentScheduler(models.Model):
    data_pagamento = models.DateField(
        blank=False,
        null=False,
        validators=[date_validate],
    )
    permite_recorrencia = models.BooleanField(blank=False, null=False)
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()

    def __str__(self):
        return f"Agendamento de pagamento {self.data_pagamento} com status {self.status_recorrencia}"
