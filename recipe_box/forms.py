from django.forms import ModelForm
from recipe_box.models import Author, Recipe

class AuthorForm(ModelForm):
    class Meta():
        model = Author
        fields = ['name', 'bio']

class RecipeForm(ModelForm):
    class Meta():
        model = Recipe
        fields = ['title', 'author', 'description', 'time_required', 'instructions']




