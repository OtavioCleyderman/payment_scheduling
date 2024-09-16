from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import PaymentScheduler
from datetime import date


class PaymentSchedulerModelTestCase(TestCase):

    def test_create_model_valid(self):
        model = PaymentScheduler(
            data_pagamento="2024-10-19",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Em andamento",
            agencia=2,
            conta=123,
            valor_pagamento=100,
        )

        try:
            model.full_clean()
            model.save()
        except ValidationError:
            self.fail("full_clean() levantou ValidationError inesperadamente!")

    def test_create_model_negative_payment(self):
        model = PaymentScheduler(
            data_pagamento="2024-10-19",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Em andamento",
            agencia=2,
            conta=123,
            valor_pagamento=-20,
        )

        # Verificar se ValidationError é levantada
        with self.assertRaises(ValidationError):
            model.full_clean()

    def test_create_model_zero_payment(self):
        model = PaymentScheduler(
            data_pagamento="2024-10-19",
            permite_recorrencia=True,
            quantidade_recorrencia=5,
            intervalo_recorrencia=30,
            status_recorrencia="Em andamento",
            agencia=2,
            conta=123,
            valor_pagamento=0,
        )

        # Verificar se ValidationError é levantada
        with self.assertRaises(ValidationError):
            model.full_clean()
