from rest_framework import serializers
from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id','name', 'alter_ego', 'primary_ability', 'second_ability', 'catchphrase', 'super_type']