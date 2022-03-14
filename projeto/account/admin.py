from django.contrib import admin

from account.models import BaseUser, Aluno, Funcionario



admin.site.register(BaseUser)

admin.site.register(Aluno)
admin.site.register(Funcionario)
