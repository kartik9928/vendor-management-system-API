from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from core import models

class ModelTest(TestCase):

    def test_vendor_creation(self):

        vendor_code = "wbfjwehbf"
        name = "kartik"
        contact_details = "1234567890"
        address = "ponda goa"
        on_time_delivery_rate = 5.5
        quality_rating_avg = 5.4
        average_response_time = 34.2
        fulfillment_rate = 9.4

        user = get_user_model().objects.create_vendor(
            vendor_code = vendor_code,
            name = name,
            contact_details = contact_details,
            address = address,
            on_time_delivery_rate = on_time_delivery_rate,
            quality_rating_avg = quality_rating_avg,
            average_response_time = average_response_time,
            fulfillment_rate = fulfillment_rate
        )

        self.assertEquals(user.vendor_code, vendor_code)

        return user

    def test_purchase_order(self):

        user = self.test_vendor_creation()
        time = timezone.now()
        json_data = {
            "name": "laptop",
            "name": "laptop",
            "name": "laptop",
        }

        order = models.PurchaseOrder.objects.create(
            po_number = 'fwerjfnwerf',
            vendor = user,
            order_date = time,
            delivery_date = time,
            items = json_data,
            quantity = 5,
            status = 'completed',
            quality_rating = 0,
            issue_date = time,
            acknowledgment_date = None
        )

        self.assertEquals(order.vendor, user)

    def test_historical_performance(self):

        user = self.test_vendor_creation()
        time = timezone.now()

        perfor = models.HistoricalPerformance.objects.create(
            vendor = user,
            date = time,
            on_time_delivery_rate = 3.5,
            quality_rating_avg = 5.3,
            average_response_time = 3.6,
            fulfillment_rate = 6.3
        )

        self.assertEquals(perfor.vendor, user)