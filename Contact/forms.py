from .models import Contact, PhoneNumber
from django import forms
from django.forms.models import inlineformset_factory


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


PhoneNumberFormSet = inlineformset_factory(Contact, PhoneNumber, form=PhoneNumberForm, extra=4)
