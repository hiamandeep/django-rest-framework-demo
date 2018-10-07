# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def home(request):
	return render(request,'index.html',{})

def another(request):
	return render(request,'another.html',{})

class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

def logoutView(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


