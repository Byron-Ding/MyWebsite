"""
URL configuration for DjangoProjectRoot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.urls import include  # Import include for URL routing
from django.views.generic import RedirectView  # Import RedirectView for root URL redirection


# Typing Support
from django.urls import URLPattern, URLResolver  # Add this import
from typing import List  # Add this import

from . import views as introduction_page_app_view

urlpatterns: List[URLPattern | URLResolver] = [
    # Home page
    path('', introduction_page_app_view.introduction_page, name='introduction_page'),
]

