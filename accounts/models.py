from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Vaga(models.Model):
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
    escolaridade_minima = models.CharField(max_length=20, choices=NIVEIS_EDUCACACIONAIS)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


class Candidatura(models.Model):
    EXPECTATIVA_SALARIAL = [
        ("0-1000", "Até 1.000"),
        ("1000-2000", "De 1.000 a 2.000"),
        ("2000-3000", "De 2.000 a 3.000"),
        ("3000+", "Acima de 3.000"),
    ]

    NIVEL_EDUCACIONAL = [
        ("fundamental", "Fundamental"),
        ("medio", "Médio"),
        ("tecnologo", "Tecnólogo"),
        ("superior", "Superior"),
        ("pos", "Pós/MBA/Mestrado"),
        ("doutorado", "Doutorado"),
    ]

    vaga = models.ForeignKey(
        Vaga, on_delete=models.CASCADE, related_name="candidaturas"
    )
    candidato = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="candidaturas"
    )
    expectativa_salarial = models.CharField(max_length=10, choices=EXPECTATIVA_SALARIAL)
    experiencia_profissional = models.TextField()
    ultima_escolaridade = models.CharField(max_length=10, choices=NIVEL_EDUCACIONAL)
    data_aplicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidato.username} - {self.vaga.titulo}"
