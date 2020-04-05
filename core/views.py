from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

#R_F

from .models import PARTNER
from rest_framework import viewsets
from .serializers import PARTNERSerializer

def home(request):

    if request.method=='POST' and 'FORMULARIO_AGREGAR' in request.POST:
        
        REQUEST_PARTNER = PARTNER()

        REQUEST_PARTNER.USU_RUT = request.POST.get('REQUEST_RUT')
        REQUEST_PARTNER.USU_NOMBRE = request.POST.get('REQUEST_NOMBRE')
        REQUEST_PARTNER.USU_APELLIDO = request.POST.get('REQUEST_APELLIDO')
        REQUEST_PARTNER.USU_CORREO = request.POST.get('REQUEST_CORREO')
        REQUEST_PARTNER.USU_CONTRASENIA = request.POST.get('REQUEST_CONTRA')
        REQUEST_PARTNER.save()
        
    
    return render(request, 'core/home.html')


class PARTNERViewSet(generics.ListAPIView):

    queryset = PARTNER.objects.all()
    serializer_class = PARTNERSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['USU_RUT', 'USU_CONTRASENIA']
    
        