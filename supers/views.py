from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from super_types.models import Super_types
from .serializers import SupersSerializer
from .models import Supers 
from django.shortcuts import get_object_or_404

# Create your views here.

# @api_view(['GET'])
# def supers_list(resquest):


#     return Response('ok')

@api_view(['GET', 'POST'])

def get_all_villains(request):

    super_villain = Super_types.objects.all()
    if request.methed == 'GET':   
        return Response(super_villain)

@api_view(['GET', 'POST'])
def get_all_hero(request):

    super_hero = Super_types.objects.all()

    if request.method == 'GET':
        return Response(super_hero)    


@api_view(['GET', 'POST'])
def supers(request):

    super_power = Supers.objects.all()


    if request.method == 'GET':

        serializer = SupersSerializer(super_power, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
    
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
   
    super_power = get_object_or_404(Supers, pk=pk)
    
    if request.method == 'GET':
            
            serializer = SupersSerializer(super_power)
            return Response(serializer.data)
            
    elif request.method == 'PUT':
            serializer = SupersSerializer(super, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
