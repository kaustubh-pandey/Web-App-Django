"""swp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = 'admin'),
    url(r'^$', views.index, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^dashboard/', include('dashboard.urls'), name = 'dashboard'),
    url(r'^orders/', include('orders.urls'), name = 'orders'),
    url(r'^medical/', include('medical.urls'), name = 'medical'),
    url(r'^hostel/',include('hostel.urls'),name='hostel'),
    url(r'^mess/',include('mess.urls'),name='mess'),
    url(r'^hostel_admin/', include('hostel_admin.urls'), name = 'hostel_admin'),
	url(r'^mess_admin/', include('mess_admin.urls'), name = 'mess_admin'),
    url(r'^medical_admin/', include('medical_admin.urls'), name = 'medical_admin'),
    url(r'^auth/callback/', include('api_integration.urls'), name = 'api_integration')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
