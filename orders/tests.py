from django.test import TestCase
from .models import Order, Customer

class OrderModelTest(TestCase):
    def setUp(self):
        # Create a customer instance to use in the Order
        self.customer = Customer.objects.create(name="John Doe", email="john.doe@example.com")
        # Create an Order instance
        self.order = Order.objects.create(
            customer=self.customer,
            item="Test Item",
            amount=100.00
        )

    def test_order_creation(self):
        # Fetch the order we created
        order = Order.objects.get(id=self.order.id)
        # Check that the order details are correct
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.item, "Test Item")
        self.assertEqual(order.amount, 100.00)


