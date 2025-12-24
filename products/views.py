from django.shortcuts import render


from rest_framework import viewsets, filters
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    search_fields = ['name', 'category__name']
    filterset_fields = ['category']

