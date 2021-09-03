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
from django.conf.urls import include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework import routers
from saas_profile.views import ApiLoginView, ApiRegisterView, ApiAuthView
from saas import settings


api_router = routers.DefaultRouter()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    # path('auth/', include('rest_framework.authtoken')),
    path('api/login/', ApiLoginView.as_view()),
    path('api/register/', ApiRegisterView.as_view()),
    path('api/auth/', ApiAuthView.as_view()),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    # pages
    path('home/', TemplateView.as_view(template_name='home.html'), name='home_page'),
    path('videos/', TemplateView.as_view(template_name='videos.html'), name='videos_page'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact_page'),
    path('review/', TemplateView.as_view(template_name='review.html'), name='review_page'),
    path('', TemplateView.as_view(template_name='login.html'), name='login_page'),
]

# urlpatterns += api_router.urls