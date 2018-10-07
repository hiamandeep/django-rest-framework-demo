# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth import login, logout, authenticate



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