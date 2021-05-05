from django import forms
from .models import Weapon


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = '__all__'
        # labels={
        #     'name':'',
        #     'number':'',
        #     'image':'',
        # }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Title...",
                    "style": "border-radius:50px",
                }
            ),
            'number': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Title...",
                    "style": "border-radius:50px",
                }
            ),
             'total': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your Title...",
                    "style": "border-radius:50px",
                }
            ),
            'image': forms.FileInput(
                attrs={
                    "class": "form-control",
                    "style": "border-radius:50px",
                }
            ),
           
        }
