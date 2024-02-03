from django.shortcuts import render,reverse
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *

def product(request):
    context = {'products': Product.objects.all()}  #
    return render(request, 'pages/product.html', context)

def productDetail(request, productID):
    product_instance = Product.objects.get(id=productID)
    context = {'product': product_instance}
    if product_instance:
        return render(request, 'pages/productDetail.html', context)
    return HttpResponse('<span style="color:red">Product not found</span>')


def addproduct(request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        thumbnail = request.POST.get('Thumbnail')

       
        Product.objects.create(
            id=product_id,
            title=title,
            price=price,
            category=category,
            thumbnail=thumbnail
        )
        r=reverse("product")
        return HttpResponseRedirect(r)
    return render(request, 'pages/addproduct.html')
  


def about(request):
    return render(request, 'pages/about.html')



def deleteproduct(request, productID):
    Product.objects.filter(id=productID).delete()
    return HttpResponseRedirect(reverse("product"))
    
     