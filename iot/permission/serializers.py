from rest_framework import serializers
from permission.models import *
import datetime
import re

#用于注册的时候返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    '''
    注册和邮箱验证码序列化
    '''
    class Meta:
        model = EmailCode
        fields = '__all__'

    REGEX_EMAIL = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

    def validate_email(self, input_email):
        '''
        验证邮箱
        '''
        # 验证邮箱是否合法
        if not re.match(self.REGEX_EMAIL, input_email):
            raise serializers.ValidationError('邮箱非法'+input_email)
        # 邮箱是否注册
        if User.objects.filter(email=input_email).count():
            raise serializers.ValidationError('用户已经存在')
        one_minute_range = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)
        if EmailCode.objects.filter(send_time__gt=one_minute_range, email=input_email, send_type='register').count():
            raise serializers.ValidationError('距离上一次发送未超过60秒')
        return input_email
