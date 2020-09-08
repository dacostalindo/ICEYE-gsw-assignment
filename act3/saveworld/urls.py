from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.saveworldView),
    path('insert/', views.insert_saveworld_item, name='insert_saveworld_item'),
    path('savior/', views.insert_savior, name='insert_savior'),
    path('delete/<int:saveworld_id>', views.delete_saveworld_item, name="delete_saveworld_item"),

]
