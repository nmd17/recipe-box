from django.forms import ModelForm
from recipe_box.models import Author, Recipe
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AuthorForm(ModelForm):
    class Meta():
        model = Author
        fields = ['name', 'bio']

class RecipeForm(ModelForm):
    class Meta():
        model = Recipe
        fields = ['title', 'author', 'description', 'time_required', 'instructions']

class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))






