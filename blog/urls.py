from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
]

handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
handler403 = 'blog.views.handler403'
handler405 = 'blog.views.handler405'