from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('completed/<int:pk>', views.UpdateTaskStatus.as_view(), name='completed'),
    path('uncompleted/<int:pk>', views.UpdateTaskStatus.as_view(), name='uncompleted'),
    path('edit/<int:pk>', views.EditTask.as_view(), name='edit'),
]
