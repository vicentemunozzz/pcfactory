from rest_framework import serializers
from .models import PARTNER

class PARTNERSerializer(serializers.ModelSerializer):

    class Meta:

        model = PARTNER
        fields = '__all__' 
        
         
         

    