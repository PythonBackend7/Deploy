from django.urls import path
from .views import TodoList, TodoDetail, PostList, PostDetail

urlpatterns = [
    path('', TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
