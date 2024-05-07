from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from vendor.serializers import VendorSerializers, performanceSerializer, VendorSerializersCrease
from django.contrib.auth import get_user_model
from core.models import HistoricalPerformance
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
import secrets


def generate_vendor_code():
    while True:
        vendor_code = secrets.randbelow(10**6)
        if len(set(str(vendor_code))) == 6:
            return f'{vendor_code:06d}'

@api_view(['POST'])
def CreateVendorView(request):
    if request.method == 'POST':
        request.data['vendor_code'] = generate_vendor_code()
        serializer = VendorSerializersCrease(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_user_model().objects.get(vendor_code = request.data['vendor_code'])
            token = Token.objects.create(user=user)
            response_data = {'token': token.key}
            return Response(response_data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def RetrieveVendorView(request, vendor_code=None):
    if request.method == 'GET':
        if vendor_code:
            queryset = get_user_model().objects.filter(vendor_code=vendor_code)
            if queryset:
                serializer = VendorSerializers(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("vendor does not found", status=status.HTTP_404_NOT_FOUND)
        else:
            queryset = get_user_model().objects.all()
            serializer = VendorSerializers(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['PUT','DELETE'])
# @permission_classes([AllowAny])
def UpdateVendorView(request, vendor_code):
    try:
        gotData = get_user_model().objects.get(vendor_code=vendor_code)
    except :
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
    if gotData:
        if request.method == 'PUT':
            serializer = VendorSerializersCrease(gotData, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            gotData.delete()
            return Response({"success": "Object deleted successfully"}, status=status.HTTP_200_OK)
    else:
        return Response("vendor does not found", status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def vendor_performance(request, vendor_code):
    try:
        get_data = get_user_model().objects.get(vendor_code=vendor_code)
    except :
        return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = HistoricalPerformance.objects.filter(vendor=get_data)
        serializer = performanceSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

