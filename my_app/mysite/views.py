from django.shortcuts import render
from .models import Bd
from .models import Rubric


def index (request):
    bbs = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics': rubrics}
    return render(request, 'mysite/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'mysite/by_rubric.html', context)

from django.views.generic.edit import CreateView

from .forms import BdForm
from django.urls import reverse_lazy

class BdCreateView(CreateView):
    template_name = 'mysite/create.html'
    form_class = BdForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric']= Rubric.objects.all()
        return context


