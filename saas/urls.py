"""saas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views
# from saas.views import login
from saas_profile.views import ApiLoginView, ApiRegisterView #, UserVS, ModPrivilegesVS


api_router = routers.DefaultRouter()
# api_router.register('user_accounts', UserVS)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', login),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/login/', ApiLoginView.as_view()),
    path('api/register/', ApiRegisterView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]

urlpatterns += api_router.urls