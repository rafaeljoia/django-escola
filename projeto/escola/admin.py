from django.contrib import admin

# Register your models here.
from escola.models import Turma, TurmaAluno

admin.site.register(Turma)
admin.site.register(TurmaAluno)