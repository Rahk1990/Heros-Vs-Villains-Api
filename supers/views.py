from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers 
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def supers_list(resquest):


    return Response('ok')
