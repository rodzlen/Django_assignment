"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include


from todo_list import views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    path('todo/',views.todo_list, name='todo_list' ),
    path('todo/<int:pk>/',views.todo_info, name='todo_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/create/', views.todo_create, name='todo_create'),
    path('todo/update/<int:pk>', views.todo_update, name='todo_update'),
    path('todo/delete/<int:pk>', views.todo_delete, name='todo_delete'),

    path('sign_up/', users_views.sign_up, name='sign_up'),
    path('login/', users_views.login, name='login'),

]
