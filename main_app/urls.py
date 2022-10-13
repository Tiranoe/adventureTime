from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('posts/create/', views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update',views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete',views.PostDelete.as_view(), name="post_delete"),
    path('posts/<int:pk>/attractions/new/', views.AttractionCreate.as_view(), name="attraction_create"),
]