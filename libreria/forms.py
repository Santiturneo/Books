from django import forms
from .models import Libro
from django.contrib.auth.forms import UserCreationForm
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass