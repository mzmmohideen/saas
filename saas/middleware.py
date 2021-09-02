# Middleware to check if the auth token is valid, which is
# present in the request's X-AUTH-TOKEN header using requests library
import json
import os

import requests
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.utils.cache import add_never_cache_headers

from saas.settings import STATIC_URL, MEDIA_URL, BASE_DIR, SHOTBOT_MEDIA_URL


def fetch_token(request):
    try:
        return request.COOKIES.get('token', None)
    except AttributeError:
        return None


def check_token(token):
    if token is None:
        return None
    req = requests.get("/auth/me/",
        headers={'Authorization': "Token {}".format(token)}
    )
    if req.status_code == 200:
        return True
    return False


class SaasMiddleware(object):
    def process_request(self, request):
        # fetch the path and token
        path = request.path
        token = fetch_token(request)
        privilege_class = request.COOKIES.get('privilege_class', None)
        # ignore all static files
        if (path.startswith(STATIC_URL)):
            return None
        if not check_token(token) and path != reverse('login_page'):
            return HttpResponsePermanentRedirect(reverse('login_page'))
        # print "Path: {}, token: {} is_valid: {}".format(request.path_info, token, check_token(token))
        # if we find a valid token
        if check_token(token) and path == reverse('login_page'):
            return HttpResponsePermanentRedirect(reverse('user_timecard'))
        return None

    def process_response(self, request, response):
        add_never_cache_headers(response)
        return response
