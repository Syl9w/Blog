from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    NewPostView, 
    UpdatePostView, 
    DeletePostView
)
urlpatterns = [
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name="post_delete"),
    path('post/<int:pk>/update/', UpdatePostView.as_view(), name = 'post_update'),
    path('post/new/', NewPostView.as_view(), name = 'post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name ='post_detail'),
    path('', BlogListView.as_view(), name = 'home'),
]