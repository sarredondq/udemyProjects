from django import forms
from .models import Page


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden  '}),
        }
        labels = {
            'title': '', 'order': '', 'content': ''
        }



FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
nombres = Page.objects.all()
tupla = ()
tupla2 = ()
for n in nombres:
    tupla = ("", n.title)
    tupla2 = (tupla,) + tupla2



class SimpleForm(forms.Form):
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=tupla2,
    )
