from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

from olx_api.serializers import UserSerializer,VechicleSerializer
from vechiles.models import Vechiles

# Create your views here.


class UserCreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class VechicleViewSet(ViewSet):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def create(self,request,*args,**kwargs):
        serializer = VechicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Vechiles.objects.get(id=id)
        serializer = VechicleSerializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def list(self,request,*args,**kwargs):
        qs = Vechiles.objects.all()
        serializer = VechicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs): # not correct (any user can retrieve any data)
        id = kwargs.get("pk")
        qs = Vechiles.objects.get(id=id)
        serializer = VechicleSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self,request,*args,**kwargs): # not correct (anyone can delete any vechicle)
        id = kwargs.get("pk")
        Vechiles.objects.get(id=id).delete()
        return Response(data={"msg":"vechicle deleted"})