from django.shortcuts import render

from apps.contacts.models import Contact


def get_contact(request):
    contact = Contact.objects.all()
    return render(request,  {'contact': contact})