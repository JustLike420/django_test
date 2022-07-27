from django import forms
from .models import Object


class ObjectCreateForm(forms.ModelForm):
    time_created = forms.TimeInput(attrs={'type': 'time'})

    class Meta:
        model = Object
        fields = ('priority', 'status', 'time_created', 'users')
