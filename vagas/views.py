from django.shortcuts import render, get_object_or_404
from .models import Vaga


# Create your views here.
def vaga_detalhes(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    candidaturas = vaga.candidaturas.all()
    context = {
        "vaga": vaga,
        "candidaturas": candidaturas,
    }

    return render(request, "vagas/vaga_detalhes.html", context)
