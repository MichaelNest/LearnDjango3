from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import Bboard, Rubric
from django.urls import reverse_lazy

def index(request):
    # bb = Bboard.objects.order_by('-published')
    bb = Bboard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'object_list': bb, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bboard.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    # success_url = 'bboard/index.html'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

