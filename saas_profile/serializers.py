from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


user_model = get_user_model()

class SER_User(serializers.ModelSerializer):

    class Meta:
        model = user_model
