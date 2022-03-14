from django.urls import path

from . import views


urlpatterns = [
    path('turmas', views.TurmaListView.as_view(),
         name='turma-list'),
]