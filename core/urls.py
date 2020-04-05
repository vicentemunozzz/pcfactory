from django.urls import path , include
from .views import home , PARTNERViewSet
from rest_framework import routers



urlpatterns = [

    path('', home , name="home"),
    path('api/PARTNER/', PARTNERViewSet.as_view()),

]
