from django.db import models


# Create your models here.
class PaymentScheduler(models.Model):
    data_pagamento = models.DateField(blank=False, null=False)
    permite_recorrencia = models.BooleanField(blank=False, null=False)
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()

    def __str__(self):
        return f"Agendamento de pagamento para {self.data_pagamento} com recorrência {self.status_recorrencia}"
