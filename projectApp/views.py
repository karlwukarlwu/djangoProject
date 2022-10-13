from django.shortcuts import render

from .models import GeeksModel
from .forms import GeeksForm


# Create your views here.

def create_view(request):
    context = {}

    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'create_view.html', context)

'''
PS C:/Users/23584/Desktop/djangoProject> python manage.py shell

>>> from projectApp.models import GeeksModel

>>> GeeksModel.objects.create(title = "title1",description="description1").save() 
>>> GeeksModel.objects.create(title = "title2",description="description2").save()  
>>> GeeksModel.objects.create(title = "title3",description="description3").save() 
>>>   
'''
def list_view(request):
    context = {}
    context["dataset"] = GeeksModel.objects.all()
    return render(request, "list_view.html", context)


# def index(request):
#     return None
