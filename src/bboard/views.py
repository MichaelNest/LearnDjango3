from django.shortcuts import render
from .models import Bboard

def index(request):
    # bb = Bboard.objects.order_by('-published')
    bb = Bboard.objects.all()
    context = {'object_list': bb}
    return render(request, 'bboard/index.html', context)
