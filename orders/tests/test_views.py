# File: orders/tests/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Customer, Order

class CustomerViewSetTest(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD123",
            email="john@example.com"
        )
        self.customer_url = reverse('customer-list')  # Update with the correct URL name

    def test_get_customers(self):
        response = self.client.get(self.customer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        data = {"name": "Jane Doe", "code": "JD124", "email": "jane@example.com"}
        response = self.client.post(self.customer_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

class OrderViewSetTest(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD123",
            email="john@example.com"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            item="Laptop",
            amount=1500.00
        )
        self.order_url = reverse('order-list')  # Update with the correct URL name

    def test_get_orders(self):
        response = self.client.get(self.order_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_order(self):
        data = {"customer": self.customer.id, "item": "Phone", "amount": 500.00}
        response = self.client.post(self.order_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
