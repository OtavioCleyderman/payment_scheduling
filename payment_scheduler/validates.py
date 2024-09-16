from django.core.exceptions import ValidationError
from datetime import datetime


def date_validate(value):
    data_atual = datetime.now()
    data_atual_formatada = data_atual.date()
    if value <= data_atual_formatada:
        raise ValidationError("Para agendamento, escolha uma data futura.")
