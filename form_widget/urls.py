from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

	path('demo/', views.demo,name='new_entry'),
	path('show/', views.show),
	path('edit/<int:id>', views.edit, name='edit'),
	path('delete/<int:id>', views.delete, name='delete'),

    ]