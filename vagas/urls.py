from django.urls import path
from . import views

urlpatterns = [
    path("<int:vaga_id>/", views.vaga_detalhes, name="vaga_detalhes"),
]
