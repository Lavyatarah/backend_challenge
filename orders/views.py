# File: /home/lavy/backend_challenge/orders/views.py
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.http import HttpResponse

# Define the index view
def index(request):
    return HttpResponse("Welcome to the Home Page!")

# Define the viewsets for your models
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
