from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        # fields='__all__'
        exclude=[
            'user'
        ]
        labels={
            'profile':'Change Profile Below'

        }
       
        widgets = {
            "profile": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your file...",
                    "style": "border-radius:50px",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your file...",
                    "style": "border-radius:50px",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Your location...",
                    "style": "border-radius:50px",
                }
            ),
        }
        

    # profile=forms.ImageField(required=False)
