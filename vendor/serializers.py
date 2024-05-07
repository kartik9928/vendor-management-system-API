from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import HistoricalPerformance


class VendorSerializersCrease(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['vendor_code', 'name', 'contact_details', 'address'] #, 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

    def create(self, data):
        return get_user_model().objects.create_vendor(**data)

class VendorSerializers(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['vendor_code', 'name', 'contact_details', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']


class performanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformance
        fields = ['vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']