from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Super_typesSerializer
from .models import Super_types
from django.shortcuts import get_object_or_404

# Create your views here.

# @api_view(['GET'])
# def super_types_list(resquest):


#     return Response('ok')

@api_view(['GET', 'POST'])
def super_types_list(request):

    super_types = Super_types.objects.all()


    if request.method == 'GET':

        serializer = Super_typesSerializer(super_types, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
    
        serializer = Super_typesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def super_types_detail(request, pk):
   
    super_type = get_object_or_404(Super_types, pk=pk)
    
    if request.method == 'GET':
            
            serializer = Super_typesSerializer(super_type)
            return Response(serializer.data)
            
    elif request.method == 'PUT':
            serializer = Super_typesSerializer(super_type, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
