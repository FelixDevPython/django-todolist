from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:task_id>/resolve/', views.mark_resolved, name='mark_resolved'),
]

