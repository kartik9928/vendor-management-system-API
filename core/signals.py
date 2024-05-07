from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import PurchaseOrder, HistoricalPerformance
from django.contrib.auth import get_user_model
import datetime
from django.utils import timezone

updated_data = []

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_delivery_rate(sender, instance, created, **kwargs):
    # if created:
    total_completed = PurchaseOrder.objects.filter(status='completed').count()
    user = get_user_model().objects.get(vendor_code=instance.vendor)
    if total_completed != 0:
        # for user in users:
        total_completed_orders = PurchaseOrder.objects.filter(vendor=user, status='completed').count()
        if total_completed_orders != 0:
            total_order_count = total_completed / total_completed_orders
        else:
            total_order_count = 0
        user.on_time_delivery_rate = total_order_count
        updated_data.append(total_order_count)
        user.save()

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_quality_rate(sender, instance, created, **kwargs):
    # if created:
    user = get_user_model().objects.get(vendor_code=instance.vendor)
    # for user in users:
    quality_rate_data = PurchaseOrder.objects.filter(vendor=user, status='completed').values('quality_rating')
    list_of_quality_rate = [item['quality_rating'] for item in quality_rate_data]
    rate_sum = sum(list_of_quality_rate)
    if rate_sum != 0:
        avg = rate_sum/len(list_of_quality_rate)
    else:
        avg = 0
    user.quality_rating_avg = avg
    updated_data.append(avg)
    user.save()


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_response_time(sender, instance, created, **kwargs):
    # if created:
    user = get_user_model().objects.get(vendor_code=instance.vendor)
    # for user in users:
    total_records = PurchaseOrder.objects.filter(vendor=user).exclude(acknowledgment_date__isnull=True).values('issue_date', 'acknowledgment_date')
    if total_records:
        deff_time = []
        for i in total_records:
            deff_time.append((i['acknowledgment_date'] - i['issue_date']).days)
        calculated_response = sum(deff_time)/len(deff_time)
    else:
        calculated_response = 0
    user.average_response_time = calculated_response
    updated_data.append(calculated_response)
    user.save()


@receiver(post_save, sender=PurchaseOrder)
def update_vendor_fulfil_rate(sender, instance, created, **kwargs):
    # if created:
    user = get_user_model().objects.get(vendor_code=instance.vendor)
    # for user in users:
    total_records = PurchaseOrder.objects.filter(vendor=user).count()
    total_completeds = PurchaseOrder.objects.filter(vendor=user, status='completed').count()
    if total_completeds != 0:
        fulfilment_rate = total_records/total_completeds
    else:
        fulfilment_rate = 0
    user.fulfillment_rate = fulfilment_rate
    updated_data.append(fulfilment_rate)
    user.save()


@receiver(post_save, sender=PurchaseOrder)
def create_performance_history(sender, instance, created, **kwargs):
    # if created:
    user = get_user_model().objects.get(vendor_code=instance.vendor)
    print("updated_data in performance : ",updated_data)

    performance_update = HistoricalPerformance.objects.create(
        vendor = user,
        date = timezone.now(),
        on_time_delivery_rate = int(updated_data[0]),
        quality_rating_avg = int(updated_data[1]),
        average_response_time = int(updated_data[2]),
        fulfillment_rate = int(updated_data[3])
    )
    performance_update.save()
