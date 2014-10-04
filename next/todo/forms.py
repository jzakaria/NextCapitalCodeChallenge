from todo.models import Item
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class ItemForm(forms.Form):
	title = forms.CharField(max_length=250, required=True)
	due = forms.DateTimeField()
