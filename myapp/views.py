# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

def home(request):
	return render(request,'index.html',{})

def another(request):
	return render(request,'another.html',{})

class ProductView(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

