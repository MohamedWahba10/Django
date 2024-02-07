from django.shortcuts import render,reverse
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
from .forms import *

def product(request):
    
    context = {'products':Product.product_list()}  
    return render(request, 'pages/product.html', context)

def productDetail(request, productID):
    product_instance = Product.product_details(productID)
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
        image = request.FILES.get('image') 

       
        Product.objects.create(
            id=product_id,
            title=title,
            price=price,
            category=category,
            image=image
        )
        r=reverse("product")
        return HttpResponseRedirect(r)
    return render(request, 'pages/addproduct.html')
  



from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MYform
from .models import Product

def formvalidation(request):
    context = {'form': MYform()}

    if request.method == "POST":
        form = MYform(request.POST, request.FILES)

        if form.is_valid():
            product_id = form.cleaned_data['id']
            title = form.cleaned_data['title']
            price = form.cleaned_data['price']
            category = form.cleaned_data['category']
            image = form.cleaned_data['image']

            Product.objects.create(
                id=product_id,
                title=title,
                price=price,
                category=category,
                image=image
            )

            return HttpResponseRedirect(reverse("product"))
        else:
            context['message'] = "Complete your data, please!"

    return render(request, 'pages/formvalidation.html', context)


def about(request): 
    return render(request, 'pages/about.html')



def deleteproduct(request, productID):
    Product.objects.filter(id=productID).delete()
    return HttpResponseRedirect(reverse("product"))
    

def updateproduct(request, productID):
    # Get the existing product data
    context = {'product': Product.objects.get(id=productID)}

    if request.method == "POST":
        # Retrieve form data
        product_id = request.POST.get('id')
        title = request.POST.get('title')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FIELS('image')

        # Update the existing product in the database
        Product.objects.filter(id=productID).update(
            id=product_id,
            title=title,
            price=price,
            category=category,
            image=image
        )

        # Redirect to the product list page
        return HttpResponseRedirect(reverse("product"))

    return render(request, 'pages/updateproduct.html', context)
