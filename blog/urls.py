from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.PostAdd.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/edit/', views.EditRecipe.as_view(),
         name='post_update'),
    path('<slug:slug>/delete/', views.DeleteRecipe.as_view(), 
         name='delete_recipe'),
]
