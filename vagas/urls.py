from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:vaga_id>/", views.vaga_detalhes, name="vaga_detalhes"),
    path("nova/", views.nova_vaga, name="nova_vaga"),
]
