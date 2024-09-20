# File: orders/tests/test_models.py
from django.test import TestCase
from .models import Customer, Order

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name="John Doe",
            code="JD123",
            email="john@example.com"
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.name, "John Doe")
        self.assertEqual(self.customer.code, "JD123")
        self.assertEqual(self.customer.email, "john@example.com")

    def test_customer_str_representation(self):
        self.assertEqual(str(self.customer), "John Doe")

class OrderModelTest(TestCase):
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

    def test_order_creation(self):
        self.assertEqual(self.order.item, "Laptop")
        self.assertEqual(self.order.amount, 1500.00)
        self.assertEqual(self.order.customer.name, "John Doe")

    def test_order_str_representation(self):
        self.assertEqual(str(self.order), "Laptop - 1500.00")
