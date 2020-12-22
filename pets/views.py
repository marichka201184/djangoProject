from django.shortcuts import render

# Create your views here.
from .models import Pet, Owner


def index(request):
    return render(request, 'index.html')


def pets(request):
    qs = Pet.objects.all()
    return render(request, 'pets.html', {'pets': qs})


def owners(request):
    qs1 = Owner.objects.all()
    return render(request, 'owner.html', {'owner': qs1})
