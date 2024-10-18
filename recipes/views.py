from django.shortcuts import render

from rest_framework import generics
from .models import Recipe, User
from .serializers import RecipeSerializer, UserSerializer
from django.http import HttpResponse

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
from django.http import HttpResponse

def recipes_list(request):
    return HttpResponse("Here will be the recipes.")
