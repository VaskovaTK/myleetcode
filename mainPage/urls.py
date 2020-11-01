from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.firstPage, name = 'firstPage'),
    path('contacts/', views.contacts, name = 'contacts'),

]
