from django import forms
from .models import SiteSystem

class SiteForm(forms.ModelForm):
    class Meta:
        model = SiteSystem
        fields='__all__'

        widgets={
            'name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'enter your name'
                }
            ),
            
            'place':forms.TextInput(
                attrs={
                    'class':'form-control',
                      'placeholder':'enter your place'
                }
            )
        }