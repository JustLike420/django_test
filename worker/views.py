from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import FormView, DeleteView
from .forms import ObjectCreateForm
from .management.commands.script import UtilsMethod
from .models import Object


def home(request):
    objects = Object.objects.all()
    # print(objects.users)
    choose(request)
    return render(request, template_name='home.html', context={'objects': objects})


"""Реализация через FormView"""


# class CreateObject(FormView):
#     form_class = ObjectCreateForm
#     template_name = 'new_object.html'
#
#     def form_valid(self, form):
#         form.save()
#         return redirect('home')


def create_obj(request):
    """Метод create"""
    form = ObjectCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ObjectCreateForm()
    return render(request, 'new_object.html', {'form': form})


def delete_obj(request, obj_id=None):
    """Метод desctroy"""
    Object.objects.filter(id=obj_id).delete()
    return redirect('home')


def choose(request):
    best_obj_id = UtilsMethod().choose()
    best_obj = Object.objects.get(id=best_obj_id)
    objects = Object.objects.all()
    return render(request, template_name='home.html', context={'objects': objects, 'best_obj': best_obj})
