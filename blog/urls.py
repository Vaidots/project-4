from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]
