"""Task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from task_api.views import create_task, get_task, update_task_name, update_task_state, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda r: HttpResponse('Welcome to the Task-API!\n')),
    path('create_task/', create_task),
    path('get_task/<int:task_id>/', get_task),
    path('update_task_name/', update_task_name),
    path('update_task_state/', update_task_state),
    path('delete_task/', delete_task),
]
