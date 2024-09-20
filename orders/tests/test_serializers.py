# File: orders/tests/test_serializers.py
from django.test import TestCase
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer

class CustomerSerializerTest(TestCase):
    def setUp(self):
        self.customer_data = {"name": "John Doe", "code": "JD123", "email": "john@example.com"}
        self.customer = Customer.objects.create(**self.customer_data)
        self.serializer = CustomerSerializer(instance=self.customer)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'code', 'email']))

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.customer_data['name'])
        self.assertEqual(data['code'], self.customer_data['code'])
        self.assertEqual(data['email'], self.customer_data['email'])

class OrderSerializerTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", code="JD123", email="john@example.com")
        self.order_data = {"customer": self.customer.id, "item": "Laptop", "amount": 1500.00}
        self.order = Order.objects.create(customer=self.customer, item="Laptop", amount=1500.00)
        self.serializer = OrderSerializer(instance=self.order)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'customer', 'item', 'amount', 'time']))

    def test_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['item'], self.order_data['item'])
        self.assertEqual(data['amount'], self.order_data['amount'])
