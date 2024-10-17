from django.urls import path
from .views import RecipeListCreate, RecipeDetail, UserListCreate, UserDetail

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
