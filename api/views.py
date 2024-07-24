from django.shortcuts import render

from rest_framework import viewsets

from api.serializers import StaffsSerializer

from api.models import Staffs

# Create your views here.

class StaffViewset(viewsets.ModelViewSet):

    serializer_class=StaffsSerializer

    queryset=Staffs.objects.all()

    model=Staffs