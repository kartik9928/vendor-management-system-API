from django.urls import path
from vendor import views

urlpatterns = [
    path('create/', views.CreateVendorView, name='create'),
    path('retrieve/', views.RetrieveVendorView, name='retrieve'),
    path('retrieve/<str:vendor_code>/', views.RetrieveVendorView, name='retrieve-single'),
    path('update/<str:vendor_code>/', views.UpdateVendorView, name='update'),
    path('performance/<str:vendor_code>/', views.vendor_performance, name='performance'),
]
