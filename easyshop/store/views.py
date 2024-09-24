from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def store(request):

    context = {}

    return render(request, 'store.html', context)

def buscket(request):

    context = {}

    return render(request, 'buscket.html', context)

def checkout(request):

    context = {}

    return render(request, 'checkout.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
