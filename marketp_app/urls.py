from django.urls import path
from .views import SellerRegistration, CustomerRegistration, SellerLogin, CustomerLogin, SellerList, CustomerList

urlpatterns = [
    path('api/seller/register/', SellerRegistration.as_view(), name='seller_register'),
    path('api/customer/register/', CustomerRegistration.as_view(), name='customer_register'),
    path('api/seller/login/', SellerLogin.as_view(), name='seller_login'),
    path('api/customer/login/', CustomerLogin.as_view(), name='customer_login'),
    path('api/sellers/', SellerList.as_view(), name='seller_list'),
    path('api/customers/', CustomerList.as_view(), name='customer_list'),
    # Add more URLs for other endpoints as needed
]
