from django import forms
from .models import Movie, AddMovie


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields= ['name','desc','year','img']



class AddMovieForm(forms.ModelForm):
    class Meta:
        model=AddMovie
        fields=['name','desc','img']
