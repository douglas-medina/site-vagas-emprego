from django.contrib import admin
from .models import Vaga, Candidatura, Empresa

admin.site.register(Empresa)
admin.site.register(Vaga)
admin.site.register(Candidatura)
