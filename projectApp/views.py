from django.shortcuts import render

from .models import GeeksModel
from .forms import GeeksForm


# Create your views here.

def creat_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'create_view.html', context)

# def index(request):
#     return None
