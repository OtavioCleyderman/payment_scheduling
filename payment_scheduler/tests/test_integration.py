from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import PaymentScheduler
import random
from datetime import datetime, timedelta
from decimal import Decimal


class PaymentSchedulerIntegrationTestCase(APITestCase):
    def generate_random_payload(self):
        start_date = datetime.now()
        end_date = start_date + timedelta(days=365)
        random_date = start_date + (end_date - start_date) * random.uniform(0.01, 1)
        return {
            "data_pagamento": random_date.strftime("%Y-%m-%d"),
            "permite_recorrencia": random.choice([True, False]),
            "quantidade_recorrencia": random.randint(1, 48),
            "intervalo_recorrencia": random.randint(1, 30),
            "status_recorrencia": random.choice(
                ["Em andamento", "Concluído", "Cancelado"]
            ),
            "agencia": random.randint(1, 1000),
            "conta": random.randint(1, 10000),
            "valor_pagamento": round(random.uniform(1, 5000), 2),
        }

    def setUp(self):
        self.create_url = reverse("payment_scheduler:payment_scheduler-list")

    def test_create_and_retrieve_payment_scheduler(self):

        payload = self.generate_random_payload()

        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        agendamento_id = response.data["id"]
        retrieve_url = reverse(
            "payment_scheduler:payment_scheduler-detail", args=[agendamento_id]
        )
        response = self.client.get(retrieve_url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data_pagamento"], payload["data_pagamento"])
        self.assertEqual(
            response.data["valor_pagamento"],
            int(round(Decimal(payload["valor_pagamento"]) * 100)),
        )
