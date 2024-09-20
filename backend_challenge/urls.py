"""
URL configuration for backend_challenge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# File: /home/lavy/backend_challenge/backend_challenge/urls.py
from django.contrib import admin
from django.urls import include, path
from orders.views import index  # Import the index view correctly from orders.views

# Define the main URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),  
    path('', index, name='home'), 
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

