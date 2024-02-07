from django.urls import path
from .views import *

urlpatterns = [
    path('products/', products, name='products'),
    path('productDetail/<int:id>/', productDetail, name='productDetail'),
    path('addproduct/', add_product, name='add_product'),
    path('update/<int:id>/',update,name='update'),
    path('delete/<int:id>/',delete,name='delete')

]
