from django.shortcuts import render, get_object_or_404, \
    HttpResponseRedirect

from .models import GeeksModel
from .forms import GeeksForm
from django.views.generic.edit import DeleteView

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


def detail_view(request, id):
    context = {}

    context['data'] = GeeksModel.objects.get(id=id)
    return render(request, 'detail_view.html', context)


def update_view(request, id):
    context = {}

    obj = get_object_or_404(GeeksModel, id=id)
    form = GeeksForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    context["form"] = form
    return render(request, "update_view.html", context)

class GeeksDeleteView(DeleteView):
    model = GeeksModel
    success_url = "/"

    template_name = "geeks/geeksmodel_confirm_delete.html"


# def index(request):
#     return None
