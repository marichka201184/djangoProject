from django import forms

from .models import Pet, Owner


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'age', 'breed', 'owner_name')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name', 'age', 'pet_name')