from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):

    context={}
    return render(request, 'user/home.html', context)