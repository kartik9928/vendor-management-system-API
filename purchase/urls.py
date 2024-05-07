from django.urls import path
from purchase import views

urlpatterns = [
    path('create/', views.createPurchase.as_view(), name='create'),
    path('display/', views.list_purchase, name='display'),
    path('display/<str:vendor_code>/', views.list_purchase, name='display_single'),
    path('order/<str:po_code>/', views.display_order, name='order'),
    path('update/<str:po_code>/', views.update_order, name='update'),
    path('acknowledge/<str:po_code>/', views.update_acknowledge, name='acknowledge'),
]
