from django import forms

class Contact(forms.Form):
    name = forms.CharField(label='Full name', max_length=20)
    email = forms.CharField(label='Email', max_length=20)
