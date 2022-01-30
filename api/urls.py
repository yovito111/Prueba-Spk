from django.urls import path
from api.views import CustomerView, SaleOrderView , SaleOrderLineView

urlpatterns = [
    path('customer/', CustomerView.as_view(), name = 'Customer_list'),
    path('customer/<int:id>', CustomerView.as_view(), name = 'customer_process'),

    path('saleorder/', SaleOrderView.as_view(), name = 'SaleOrder_list'),
    path('saleorder/<int:id>', SaleOrderView.as_view(), name = 'SaleOrder_proceess'),

     path('saleorderline/', SaleOrderLineView.as_view(), name = 'SaleOrderLine_list'),
    path('saleorderline/<int:id>', SaleOrderLineView.as_view(), name = 'SaleOrderLine_proceess'),
]  