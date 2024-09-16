from django.db import models
from .validates import date_validate
from django.core.validators import MinValueValidator
from django.db.models import UniqueConstraint


class PaymentScheduler(models.Model):
    data_pagamento = models.DateField(
        blank=False,
        null=False,
        validators=[date_validate],
    )
    permite_recorrencia = models.BooleanField()
    quantidade_recorrencia = models.IntegerField()
    intervalo_recorrencia = models.IntegerField()
    status_recorrencia = models.CharField(max_length=100)
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=[
                    "data_pagamento",
                    "agencia",
                    "conta",
                    "valor_pagamento",
                    "permite_recorrencia",
                    "quantidade_recorrencia",
                    "intervalo_recorrencia",
                    "status_recorrencia",
                ],
                name="unique_payment_scheduler",
                violation_error_message="Já existe um agendamento com esta combinação de campos.",
            ),
        ]

    def __str__(self):
        return f"Agendamento de pagamento {self.data_pagamento} com status {self.status_recorrencia}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
