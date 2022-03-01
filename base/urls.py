from django.urls import path
from .views import TaskList, Task

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', Task.as_view(), name='task'),
]