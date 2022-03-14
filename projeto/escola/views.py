from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from escola.models import Turma


class TurmaListView(ListView):

    model = Turma
    template_name = 'escola/list.html'
    context_object_name = 'turmas'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(TurmaListView, self).get_context_data(**kwargs)
        turmas = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(turmas, self.paginate_by)
        try:
            turmas = paginator.page(page)
        except PageNotAnInteger:
            turmas = paginator.page(1)
        except EmptyPage:
            turmas = paginator.page(paginator.num_pages)
        context['turmas'] = turmas
        return context