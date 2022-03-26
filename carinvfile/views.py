from django.shortcuts import render

from .models import Mechanic, ServicesTable, ShopInventory
from .serializers import MechanicSerializer,ShopInventorySerializer, serviceSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.
class InventorySnippetList(generics.ListCreateAPIView):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer


class InventorySnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopInventory.objects.all()
    serializer_class = ShopInventorySerializer



class MechanicViewSet(viewsets.ModelViewSet):
    serializer_class=MechanicSerializer

    def get_queryset(self):
        mechanic=Mechanic.objects.all()
        return mechanic

    # def create(self,request,*args,**kwargs):
    #     data=request.data
    #     new_mechanic=Mechanic.objects.create(name_of_mechanic=data['name_of_mechanic'])
    #     new_mechanic.save()
    #     for service in data['service']:
    #         service_obj=ServicesTable.objects.get(service_name=service['service'])
    #         new_mechanic.service.add(service_obj)
    #     serializer=serviceSerializer(new_mechanic)
    #     return Response(serializer.data)
class ServicesList(generics.ListCreateAPIView):
    queryset = ServicesTable.objects.all()
    serializer_class = serviceSerializer



# class MechanicList(generics.ListCreateAPIView):
#     queryset = Mechanic.objects.all()
#     serializer_class = MechanicSerializer


#     def create(self,request,*args,**kwargs):
#         data=request.data
#         new_mechanic=Mechanic.objects.create(name_of_mechanic=data['name_of_mechanic'])
#         new_mechanic.save()
#         for service in data['services']:
#             service_obj=ServicesTable.objects.get(service_name=service['services'])
#             new_mechanic.modules.add(service_obj)
#         serializer=serviceSerializer(new_mechanic)
#         return Response(serializer.data)
