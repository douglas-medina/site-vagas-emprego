from django.urls import path
from . import views

url_patterns = [
    path("vagas/<int:vaga_id>/", views.vaga_detalhes, name="vaga_detalhes"),
]
