from django.shortcuts import render
from django.http import HttpResponse
from .models import SaveItem

# Create your views here.
def saveworldView(request):
    all_saveworld_items = SaveItem.object.all()
    return render(request, 'hello.html',
        {'all_items' : all_saveworld_items })
