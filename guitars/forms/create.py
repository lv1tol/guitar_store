from django import forms
from guitars.models import Guitar

class GuitarCreateForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['brand', 'model', 'color', 'type', 'year', 'price', 'avatar', 'description']