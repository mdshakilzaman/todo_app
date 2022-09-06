from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import todos
from django.urls import reverse

def index(request):
    lists = todos.objects.all().values()
    template = loader.get_template('list.html')
    context = {
    'lists': lists,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['item']
    lists = todos(items=x)
    lists.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = todos.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def finished_task(request, id):
    member = todos.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
