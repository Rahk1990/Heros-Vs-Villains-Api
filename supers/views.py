from random import randint
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from super_types.models import Super_types
from .serializers import SupersSerializer
from .models import Supers 
from django.shortcuts import get_object_or_404

# Create your views here.

    
    # supers_detail = Supers.objects.all()
       ####Method Tester###
    # if request.method == 'GET':
    #     super_type = Supers.objects.all()              
    #     serializer = SupersSerializer(super_type, many=True)
    #     return Response(serializer.data)

@api_view(['GET', 'POST'])
def supers(request):
    if request.method == 'GET':


        
        # This will handle three scenarios:
        # http://127.0.0.1:8000/api/?type="hero" (or "villian")

        type_param = request.query_params.get('type')
        
        if type_param == "hero":
            records = Supers.objects.filter(super_type=1)
            serializer = SupersSerializer(records, many=True)
            return Response(serializer.data) 

        elif type_param == "villain":
            records = Supers.objects.filter(super_type=2)
            serializer = SupersSerializer(records, many=True)
            return Response(serializer.data)
        else:
            # If type is not passed get all records
            super_type = Supers.objects.all()              
            serializer = SupersSerializer(super_type, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status.HTTP_201_CREATED)



        # records = Supers.objects.all()
        # serializer = SupersSerializer(records, many=True)
        # return Response(serializer.data)
    # return Response(records, status.HTTP_200_OK)
            
        # return Response(records, status.HTTP_200_OK)

    # elif request.method == 'POST': #Create new hero
    #     # records = Supers.objects.get
    #     serializer = SupersSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status.HTTP_201_CREATED)
    
@api_view(['GET','PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
   
       
    
    if request.method == 'GET':
               
        serializer = SupersSerializer(super)
        return Response(serializer.data)
            
    elif request.method == 'PUT': # update supers data
        serializer = SupersSerializer(super, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE': # delete supers data
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#         @api_view(['GET'])
# def get_all_villains(request):

#     super_villain = Supers.objects.get(fk=1)
#     serializer = SupersSerializer(super_villain, many=True)

#     if request.method == 'GET':
#         return Response(serializer.data) 

# @api_view(['GET'])
# def get_all_heros(request):

#     super_heros = Super_types.objects.all()
    
#     custom_response_dictionary = {}

#     for super_hero in super_heros:

#         super_heros = Supers.objects.filter(super_id=super_hero.id)

#         super_hero_serializer = SupersSerializer(super_hero, many=True)

#         custom_response_dictionary[super_hero.name] = {
#             "type":  super_hero.super_type,
#             "super_hero": super_hero_serializer.data
#             }

#     return Response(custom_response_dictionary)

    # super_hero = Supers.objects.filter(fk=2)
    # serializer = SupersSerializer(super_hero, many=True)

    # if request.method == 'GET':
    #     return Response(serializer.data)    

