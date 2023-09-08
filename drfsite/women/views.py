from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from women.models import *
from women.serializers import *


# class WomanApiViews(generics.ListAPIView):
#     queryset = Women.get_all()
#     serializer_class = WomenSerializer
#

class WomanApiViews(APIView):
    def get(self, request):
        print(dir(request))
        lst = Women.objects.all()
        return Response({'posts': WomenSerializer(lst, many=True).data()})

    def post(self, request):
        print(request.data)
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(
            raise_exception=True)  # raise_exception is required for the client to receive a valid value in JSON format
        serializer.save()  # Method save calls method create after that in
        # instance appear new attribute data with valid data

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        print(kwargs)

        if not pk:
            return Response({'error': 'You are passed wrong query params, must be -> pk'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        # if we specify params "instance" and "data" in Serializer then when we call save
        # it will call method update instead create
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data()})




