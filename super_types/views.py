from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import Super_typesSerializer
from .models import Super_types
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET'])
def super_types_list(resquest):


    return Response('ok')