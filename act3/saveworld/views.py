from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import SaveItem, Savior

# Create your views here.
def saveworldView(request):
    context = {'saveworld_list' : SaveItem.objects.all()}
    return render(request, 'hello.html', context)


def insert_saveworld_item(request:HttpRequest):
    saveworld = SaveItem(content = request.POST['content'])
    saveworld.save()
    return redirect('/saveworld/list/')

def insert_savior(request:HttpRequest):
    savior = Savior(salute = request.POST['salute'])
    savior.save()
    return redirect('/saveworld/list/')


def delete_saveworld_item(request, saveworld_id):
    saveworld_to_delete = SaveItem.objects.get(id=saveworld_id)
    saveworld_to_delete.delete()
    return redirect('/saveworld/list/')
