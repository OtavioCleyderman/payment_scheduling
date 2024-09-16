from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import PaymentScheduler
import random
from datetime import datetime, timedelta
from decimal import Decimal


class PaymentSchedulerViewsTestCase(APITestCase):
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
        self.list_url = reverse("payment_scheduler:payment_scheduler-list")
        self.detail_url = lambda pk: reverse(
            "payment_scheduler:payment_scheduler-detail", args=[pk]
        )
        self.valid_payload = self.generate_random_payload()

        self.invalid_payload = {
            "data_pagamento": "2024-10-21",
            "permite_recorrencia": True,
            "quantidade_recorrencia": 2,
            "intervalo_recorrencia": 15,
            "status_recorrencia": "Em andamento",
            "agencia": 85,
            "conta": 6696,
            "valor_pagamento": 0,
        }

        # Objeto para o teste de listar e deletar agendamentos
        self.payment_scheduler = PaymentScheduler.objects.create(
            **self.generate_random_payload()
        )
        PaymentScheduler.objects.create(
            data_pagamento="2024-11-01",
            permite_recorrencia=False,
            quantidade_recorrencia=1,
            intervalo_recorrencia=15,
            status_recorrencia="Concluído",
            agencia=3,
            conta=456,
            valor_pagamento=150,
        )

    def test_create_valid_payment_scheduler(self):
        payload = self.valid_payload
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_object = PaymentScheduler.objects.get(id=response.data["id"])
        self.assertEqual(
            created_object.valor_pagamento,
            int(round(Decimal(payload["valor_pagamento"]) * 100)),
        )
        self.assertEqual(
            created_object.permite_recorrencia, payload["permite_recorrencia"]
        )
        self.assertEqual(response["Content-Type"], "application/json")

    def test_create_invalid_payment_scheduler(self):
        payload = self.invalid_payload
        response = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("valor_pagamento", response.data)
        self.assertEqual(response["Content-Type"], "application/json")

    def test_list_payment_schedulers(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "application/json")
        response_data = response.json()
        self.assertIsInstance(response_data, list)
        self.assertEqual(len(response_data), 2)

    def test_get_payment_schedulers(self):
        payment_scheduler = PaymentScheduler.objects.create(**self.valid_payload)
        response = self.client.get(self.detail_url(payment_scheduler.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response["Content-Type"], "application/json")

    def test_delete_payment_scheduler(self):
        pk = self.payment_scheduler.id
        response = self.client.delete(self.detail_url(pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PaymentScheduler.objects.filter(id=pk).exists())

    def test_create_duplicate_payment_scheduler(self):
        response1 = self.client.post(self.list_url, self.valid_payload, format="json")
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.client.post(self.list_url, self.valid_payload, format="json")
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        expected_error_message = "Os campos data_pagamento, agencia, conta, valor_pagamento, permite_recorrencia, quantidade_recorrencia, intervalo_recorrencia, status_recorrencia devem criar um set único."
        self.assertIn(expected_error_message, response2.data["non_field_errors"])
