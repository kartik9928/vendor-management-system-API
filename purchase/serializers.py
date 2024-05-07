from rest_framework import serializers
from core.models import PurchaseOrder
from django.contrib.auth import get_user_model
import uuid

class OrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date']

        # def create(self, validated_data):
        #     # Generate a unique po_number
        #     validated_data['po_number'] = str(uuid.uuid4().hex)[:12].upper()  # Generate a unique string of 12 characters

        #     return super().create(validated_data)

class OrderSerializersget(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'order_date', 'delivery_date', 'items', 'quantity', 'status', 'quality_rating', 'issue_date', 'acknowledgment_date']