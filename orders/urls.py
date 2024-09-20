# File: /home/lavy/backend_challenge/orders/urls.py
from django.urls import path, include
from .views import CustomerViewSet, OrderViewSet, index  # Correctly import views
from rest_framework.routers import DefaultRouter

# Set up the API router for the viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # API routes for customers and orders
    path("", index, name="orders"),      # Root path directs to the index view
]
