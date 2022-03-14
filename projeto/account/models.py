from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class BaseUser(AbstractUser):
    FUNCIONARIO = '1'
    ESTUDANTE = '2'

    mapping_users = ((FUNCIONARIO, "FUNCIONARIO"), (ESTUDANTE, "ESTUDANTE"))
    user_type = models.CharField(default=1, choices=mapping_users, max_length=10)



class Funcionario(models.Model):
    user = models.OneToOneField(BaseUser, related_name="funcionario", on_delete=models.CASCADE)
    data_admissao = models.DateField()

    def __str__(self):
        return self.user.get_full_name()


class Aluno(models.Model):
    user = models.OneToOneField(BaseUser, related_name="aluno",  on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    avatar = models.FileField()
    address = models.TextField()

    def __str__(self):
        return self.user.get_full_name()
