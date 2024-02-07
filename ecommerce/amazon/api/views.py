from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from amazon.views import *
from amazon.models import *
from amazon.forms import *
from amazon.api.serializer import *

@api_view(['GET'])
def products(request):
    data = Product.product_list()
    datajson=Amazonserlizer(data,many=True).data
    return Response({'msg': 'hello leooo', 'data': datajson})


@api_view(['GET'])

def productDetail(request,id):
    data=Product.product_details(id)
    datajson=Amazonserlizer(data).data    
    return Response({'data':datajson})

@api_view(['POST'])
def add_product(request):
    # obj = addproduct(request)  
    # obj.id = request.data['id']
    # obj.title = request.data['title']
    # obj.price = request.data['price']
    # obj.category = request.data['category']
    # obj.image = request.data['image'] 
    obj=Amazonserlizer(data=request.data)
    if(obj.is_valid()):
        obj.save()
        return Response({'msg': 'DONE'})
    return Response({'msg': 'error'})


@api_view(['PUT'])
def update(request, id):
    update_object = Product.objects.filter(id=id).first()
    if update_object:
        serializered_product = Amazonserlizer(instance=update_object, data=request.data)
        if serializered_product.is_valid():
            serializered_product.save()
            return Response(serializered_product.data)
    return Response({'msg': ''})



@api_view(['DELETE'])
def delete(request, id):
    delete_object = Product.objects.filter(id=id).first()
    if delete_object:
        delete_object.delete()
        return Response({'msg': 'Product deleted'})
    return Response({'msg': 'Product not found'})


        