from django.urls import path
from .views import RecipeListCreate, RecipeDetail, UserListCreate, UserDetail
from . import views
urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
urlpatterns = [
    path('api/token/', views.obtain_token, name='token_obtain_pair'),
    path('api/token/refresh/', views.refresh_token, name='token_refresh'),
    path('api/recipes/', views.recipes_list, name='recipes_list'),
]