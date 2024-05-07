from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from core.models import PurchaseOrder
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from purchase.serializers import OrderSerializers, OrderSerializersget
from django.utils import timezone

class createPurchase(generics.CreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = OrderSerializers


@api_view(['GET'])
def list_purchase(request, vendor_code=None):
    if request.method == 'GET':
        if vendor_code:
            user = get_user_model().objects.get(vendor_code=vendor_code)
            getData = PurchaseOrder.objects.filter(vendor=user)
            if getData:
                serializer = OrderSerializersget(getData, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("purchase not found", status=status.HTTP_404_NOT_FOUND)
        else:
            getData = PurchaseOrder.objects.all()
            serializer = OrderSerializersget(getData, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def display_order(request, po_code):
    if request.method == 'GET':
        if po_code:
            try:
                getData = PurchaseOrder.objects.get(po_number=po_code)
                serializer = OrderSerializersget(getData, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("purchase not found", status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE'])
def update_order(request, po_code):
    try:
        gotData = PurchaseOrder.objects.get(po_number=po_code)
    except :
        return Response({"error": "order not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OrderSerializers(gotData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        gotData.delete()
        return Response({"success": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_acknowledge(request, po_code=None):
    vendor = get_user_model().objects.get(vendor_code=request.user)
    original = PurchaseOrder.objects.filter(vendor=vendor, po_number=po_code)

    if original:
        for purchase_order in original:
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.quantity = 10011
            purchase_order.save()
        return Response("serializer.data")
    else:
        return Response({"error": "order not found"}, status=status.HTTP_404_NOT_FOUND)