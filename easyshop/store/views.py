from django.shortcuts import render

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