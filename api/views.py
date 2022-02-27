from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from rest_framework.decorators import api_view,action
from django.core.cache import cache

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get','post','delete','put']
    def create(self, request, format=None):
        print('in Create')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
        return Response({"status":1,"message":"in Create"})
    def list(self, request):
        print('in List  ')
        qs = self.queryset

        #z = cache.set('my_key',Product.objects.all())
        #print(z)
        serializers = self.serializer_class(qs,many=True)
        return Response({"status":1,"message":"in List","data" :serializers.data})
        #return Response({"status":1,"message":"in List "})
    def retrieve(self, request, pk=None):
        z = cache.get('key')
        print(z)
        print('in Retrieve')
        qs = Product.objects.get(pk = pk)
        serializers = self.serializer_class(qs)
        return Response({"status":1,"message":"in Retrieve","data" :serializers.data})
        #return Response({"status":1,"message":"in Retrieve"})
    def update(self, request,pk=None):
        product = Product.objects.get(pk = pk)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            profile = serializer.save()
        print('in update')
        return Response({"status":1,"message":"in update"})
    def destroy(self, request, pk=None):
        print('in destroy')
        qs = Product.objects.get(pk = pk).delete()
        return Response({"status":1,"message":"in destroy"})

    @action(methods=['put'], detail=False)
    def edit(self, request):
        return Response({"status":1,"message":"In edit"})