from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):

    title = forms.CharField(required=False)
    body=forms.CharField()
    created=forms.DateField()


class TodoUpdateForm(forms.ModelForm):
    class Meta():
        model=Todo
        fields ='__all__'