from rest_framework import serializers

from .models import User, Brassiere


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'nick_name','password','nickname')

class BrassiereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brassiere
        fields = ('bra_name', 'wash_num')