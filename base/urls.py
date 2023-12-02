from django.contrib import admin
from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('login/', views.MyTokenObtainPairView.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/<int:pk>/', views.ProductDetail.as_view()),
]
