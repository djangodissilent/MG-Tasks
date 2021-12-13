from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from task_api.views import create_task, get_task, update_task_name, update_task_state, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: HttpResponse(
        'Welcome to the Task-API!\n')),  # Welcome message
    path('create_task/', create_task),
    path('get_task/<int:task_id>/', get_task),
    path('update_task_name/', update_task_name),
    path('update_task_state/', update_task_state),
    path('delete_task/', delete_task),
]
