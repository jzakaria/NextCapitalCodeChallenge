from todo.models import Item
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class ItemForm(forms.Form):
	title = forms.CharField(max_length=250, required=True)
	date = forms.DateTimeField()


class NewUserForm(forms.Form):
	email = forms.EmailField(label="Email (this will be your username)")
	password1=forms.CharField(max_length=30,widget=forms.PasswordInput(),label="Password")
	password2=forms.CharField(max_length=30,widget=forms.PasswordInput(),label="Please repeat your password")

	def clean(self): # check if password 1 and password2 match each other
	    if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:#check if both pass first validation
	        if self.cleaned_data['password1'] != self.cleaned_data['password2']: # check if they match each other
	            raise forms.ValidationError("Passwords dont match each other")

	    return self.cleaned_data