from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list,name='order_list'),
    path('created/', views.order_create, name='order_create'),
]