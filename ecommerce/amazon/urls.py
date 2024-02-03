from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('productDetail/<int:productID>/', views.productDetail, name='productDetail'),
    path('about/', views.about, name='about'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('deleteproduct/<int:productID>/', views.deleteproduct, name='deleteproduct')
   
]
