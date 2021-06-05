# need to create this urls.py

from django.urls import path
from .import views

urlpatterns = [
	path('', views.index, name="list"),
	path('update_sticky/<str:pk>/', views.updateSticky, name="update_sticky"),
	path('delete/<str:pk>/', views.deleteSticky, name="delete"),



	path('', views.index2, name="list"),
	path('update_sticky2/<str:pk>/', views.updateSticky2, name="update_sticky2"),
	path('delete2/<str:pk>/', views.deleteSticky2, name="delete2"),

]