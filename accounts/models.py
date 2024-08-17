from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vagas(models.Model):
    FAIXAS_SALARIAIS = [
        ("0-1000", "Até 1.000"),
        ("1000-2000", "De 1.000 a 2.000"),
        ("2000-3000", "De 2.000 a 3.000"),
        ("3000+", "Acima de 3.000"),
    ]

    NIVEIS_EDUCACACIONAIS = [
        ("fundamental", "Fundamental"),
        ("medio", "Médio"),
        ("tecnologo", "Tecnólogo"),
        ("superior", "Superior"),
        ("pos", "Pós/MBA/Mestrado"),
        ("doutorado", "Doutorado"),
    ]

    empresa = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vagas")
    titulo = models.CharField(max_length=200)
    faixa_salarial = models.CharField(max_length=10, choices=FAIXAS_SALARIAIS)
    requisitos = models.TextField()
    nivel_educacional = models.CharField(max_length=20, choices=NIVEIS_EDUCACACIONAIS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
