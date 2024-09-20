from django.contrib import admin
from .models import Customer, Order

# Register the models with the admin interface
admin.site.register(Customer)
admin.site.register(Order)

