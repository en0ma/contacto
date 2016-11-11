from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Contact as ContactModel
from .forms import Contact as ContactForm
from django.core import validators

def index(request):
    return render(request, 'addressbook/index.html', {})

def list(request):
    contacts = ContactModel.objects.all()
    return render(request, 'addressbook/list.html', {'contacts': contacts})

def add(request):
    if request.method == 'POST':
        try:
            contact = ContactForm(request.POST)
            contact.is_valid()
            contact = contact.cleaned_data
            validators.validate_email(contact['email'])
            ContactModel.objects.create(name=contact['name'], email=contact['email'])
            return render(request, 'addressbook/add.html', {'success_message': 'Yay! contact added.', 'contact' : ContactForm})
        except Exception as e:
                return render(request, 'addressbook/add.html', {'contact': ContactForm, 'errors': e})
    else:
        return render(request, 'addressbook/add.html', {'contact': ContactForm})
