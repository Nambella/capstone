from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group
class User(AbstractUser):
    email = models.EmailField(unique=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=100)
    preparation_time = models.IntegerField()
    cooking_time = models.IntegerField()
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

