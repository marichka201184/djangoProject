from django.shortcuts import render

# Create your views here.
from .models import Pet, Owner
from .forms import PetForm, OwnerForm


def base(request):
    return render(request, 'base.html')

def pets(request, id):
    try:
        qs = Owner.objects.get(pk=id).pets.all()
        form = PetForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()

    # qs = Pet.objects.all()
    # print(id)
    except Exception:
        qs = None
        print(qs)
    return render(request, 'pets.html', {'pets': qs, 'form': form})


def owners(request):
    qs1 = Owner.objects.all()
    try:
        qs1 = Owner.objects.all()
        form1 = OwnerForm(request.POST)
        if request.method == 'POST':
            if form1.is_valid():
                form1.save()
    except Exception:
        qs = None
        print(qs)
    return render(request, 'owner.html', {'owner': qs1, 'form1': form1})


def calc(request, first, option, second):
    res = ''
    if option == 'add':
        res = f'{first} + {second} = {first + second}'
    elif option == 'sub':
        res = f'{first} - {second} = {first - second}'
    elif option == 'multi':
        res = f'{first} * {second} = {first * second}'
    elif option == 'div':
        try:
            res = f'{first} / {second} = {first / second}'
        except ZeroDivisionError:
            res = None
    return render(request, 'calc.html', {'res': res})
