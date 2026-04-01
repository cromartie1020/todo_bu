from . import views
from django.urls import path

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('about/', views.about, name='about'),
    path('<int:pk>/', views.todo_detail, name='todo_detail'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:pk>/update/', views.todo_update, name='todo_update'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]
