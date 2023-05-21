"""
URL configuration for infsus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from master_detail import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('computers/', views.computer_list, name='computer_list'),
    path('computers/add/', views.computer_add, name='computer_add'),
    path('computers/edit/<int:pk>/', views.computer_edit, name='computer_edit'),
    path('computers/delete/<int:pk>/', views.computer_delete, name='computer_delete'),
    path('desks/', views.desk_list, name='desk_list'),
    path('desks/add/', views.desk_add, name='desk_add'),
    path('desks/edit/<int:pk>/', views.desk_edit, name='desk_edit'),
    path('desks/delete/<int:pk>/', views.desk_delete, name='desk_delete'),
    path('components/edit/<int:pk>/', views.component_edit, name='component_edit'),
    path('components/delete/<int:pk>/', views.component_delete, name='component_delete'),
    path('components/create/<int:pk>/', views.component_create, name='component_create'),
]