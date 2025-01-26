from django import forms
from guitars.models import Guitar

class GuitarUpdateForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['brand', 'model', 'color', 'type', 'year', 'price']