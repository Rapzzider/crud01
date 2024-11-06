from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('created/', views.product_created, name='product_created'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('<int:id>/updated/', views.product_updated, name='product_updated'),
    path('<int:id>/deleted/', views.product_deleted, name='product_deleted'),
]
