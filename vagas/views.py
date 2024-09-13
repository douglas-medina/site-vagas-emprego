from django.shortcuts import render, get_object_or_404, redirect
from .models import Vaga, Candidatura, Empresa
from django.contrib.auth.decorators import login_required


def home(request):
    vagas = Vaga.objects.all()
    return render(request, "vagas/home.html", {"vagas": vagas})


@login_required
def vaga_detalhes(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    candidaturas = vaga.candidaturas.all()

    if request.method == "POST":
        expectativa_salarial = request.POST.get("expectativa_salarial")
        experiencia_profissional = request.POST.get("experiencia_profissional")
        ultima_escolaridade = request.POST.get("ultima_escolaridade")

        Candidatura.objects.create(
            vaga=vaga,
            candidato=request.user,
            expectativa_salarial=expectativa_salarial,
            experiencia_profissional=experiencia_profissional,
            ultima_escolaridade=ultima_escolaridade,
        )
        return redirect("home")

    context = {
        "vaga": vaga,
        "candidaturas": candidaturas,
        "expectativa_salarial_choices": Candidatura.EXPECTATIVA_SALARIAL,
        "nivel_educacional_choices": Candidatura.NIVEL_EDUCACIONAL,
    }
    return render(request, "vagas/vaga_detalhes.html", context)


@login_required
def nova_vaga(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        empresa_id = request.POST.get("empresa")
        faixa_salarial = request.POST.get("faixa_salarial")
        requisitos = request.POST.get("requisitos")
        escolaridade_minima = request.POST.get("escolaridade_minima")

        empresa = get_object_or_404(Empresa, id=empresa_id)
        Vaga.objects.create(
            titulo=titulo,
            empresa=empresa,
            faixa_salarial=faixa_salarial,
            requisitos=requisitos,
            escolaridade_minima=escolaridade_minima,
        )
        return redirect("home")

    empresas = Empresa.objects.all()
    return render(
        request,
        "vagas/nova_vaga.html",
        {
            "empresas": empresas,
            "faixa_salarial_choices": Vaga.FAIXAS_SALARIAIS,
            "nivel_educacional_choices": Vaga.NIVEIS_EDUCACACIONAIS,
        },
    )
