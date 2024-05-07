from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.utils import timezone

class VendorManager(BaseUserManager):

    def create_vendor(self, **kwargs):
        user = self.model(**kwargs)
        user.save(using=self._db)

        return user

class Vendor(AbstractBaseUser, PermissionsMixin):
    # vender creation

    vendor_code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    objects = VendorManager()

    USERNAME_FIELD = 'vendor_code'

STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

class PurchaseOrder(models.Model):
    # Purchase Order model

    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)


class HistoricalPerformance(models.Model):
    # Historical Performance model

    vendor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()