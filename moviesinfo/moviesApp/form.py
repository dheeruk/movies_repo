from django import forms
from .models import AddMoviesModel
class AddMovies(forms.ModelForm):
    class Meta:
        model=AddMoviesModel
        fields='__all__'
