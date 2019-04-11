from rest_framework import serializers
from permission.models import *

#用于注册的时候返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        field = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = User
        field = '__all__'

