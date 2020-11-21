from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sol, name='solutions'),
    path('solved', views.solved, name='solved'),

]