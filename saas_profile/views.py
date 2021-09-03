from django.shortcuts import render
from rest_framework import viewsets, response, status
from saas_profile.serializers import user_model, SER_User
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_auth.serializers import LoginSerializer
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.http import HttpResponse


# Create your views here.
class ApiRegisterView(RegisterView):
    serializer_class = RegisterSerializer

    def get_response_data(self, user):
        response = super(ApiRegisterView, self).get_response_data(user)
        response.update({
            'token': response.get('key'),
            'username': user.username,
            'id': user.id,
            'email': user.email
        })
        response.pop('key')
        return response

    def save(self, request):
        response = super(ApiRegisterView, self).save(request)
        additional_data = {
            'token': response.data.get('key'),
            'username': self.user.username,
            'id': self.user.id,
            'email': self.user.email
        }
        response.data = additional_data
        return response


class ApiLoginView(LoginView):
    serializer_class = LoginSerializer

    def get_response(self):
        response = super(ApiLoginView, self).get_response()
        additional_data = {
            'token': response.data.get('key'),
            'username': self.user.username,
            'id': self.user.id,
            'email': self.user.email
        }
        response.data = additional_data
        return response


class ApiAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        return HttpResponse(True)
        # try:
        #     return True
        # except:
        #     return False
        # return Response("Hello {0}!".format(request.user))