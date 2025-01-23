from django.urls import path

import cb_views

app_name= 'todo'

urlpatterns=[
    path('', cb_views.TodoListView.as_view(), name='list'),
     path('create/', cb_views.TodoCreateView.as_view(), name='create'),
     path('<int:pk>/', cb_views.TodoDetailView.as_view(), name='detail'),
     path('update/<int:pk>', cb_views.TodoUpdateView.as_view(), name='update'),
     path('delete/<int:pk>', cb_views.TodoDeleteView.as_view(), name='delete'),
]