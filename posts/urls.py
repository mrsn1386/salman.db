from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='all_posts'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
]