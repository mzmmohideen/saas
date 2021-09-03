# Middleware to check if the auth token is valid, which is
# present in the request's X-AUTH-TOKEN header using requests library
import json
import os

import requests
from django.urls import reverse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils.cache import add_never_cache_headers
from django.utils.deprecation import MiddlewareMixin

from saas.settings import STATIC_URL, BASE_DIR


def fetch_token(request):
    try:
        return request.COOKIES.get('token', None)
    except AttributeError:
        return None


def check_token(host, token):
    if token is None:
        return None
    req = requests.get(f"{host}api/auth/",
        headers={'Authorization': "Token {}".format(token)}
    )
    if req.status_code == 200:
        return True
    return False


class SaasMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # fetch the path and token
        path = request.path
        print('path', path)
        host = request.build_absolute_uri('/')
        token = fetch_token(request)
        # ignore all static files
        if path.startswith((STATIC_URL, '/rest-auth', '/api', '/admin')):
            return None
        if not check_token(host, token) and path != reverse('login_page'):
            return HttpResponsePermanentRedirect(reverse('login_page'))
        # if we find a valid token
        if check_token(host, token) and path == reverse('login_page'):
            return HttpResponsePermanentRedirect(reverse('home_page'))
        return None

    def process_response(self, request, response):
        add_never_cache_headers(response)
        return response
