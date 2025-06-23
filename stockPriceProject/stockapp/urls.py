from django.urls import path
from . import views

urlpatterns = [
    path('' , views.get_stock_price, name = "stock-price")
]
