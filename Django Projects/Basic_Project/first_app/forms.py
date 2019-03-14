from django import forms
from first_app.models import User_Info

class SignForm(forms.ModelForm):
    class Meta():
        model = User_Info
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'f_name'}),
            'last_name': forms.TextInput(attrs={'class': 'l_name'}),
            'email': forms.TextInput(attrs={'class': 'em'}),
        }
