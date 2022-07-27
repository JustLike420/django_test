from django.contrib import admin
from django.urls import path

from .views import home, create_obj, delete_obj, choose

urlpatterns = [
    path('', home, name='home'),
    path('new_obj', create_obj, name='new_obj'),
    path('delete_obj/<int:obj_id>', delete_obj, name='delete_obj'),
    path('choose', choose, name='choose'),
]
