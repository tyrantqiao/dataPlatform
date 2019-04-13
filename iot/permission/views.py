from django.shortcuts import render

from .models import *
from rest_framework import mixins,viewsets,filters,status
from .serializers import *
from .permission import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from api.CountModelMixin import CountModelMixin
from django.db.models import Count,F
from itertools import chain
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
from captcha.views import CaptchaStore, captcha_image
from .utils.captcha import *
from django.core.mail import BadHeaderError, send_mail,EmailMessage
import base64
import json
import datetime

# Create your views here.
class CaptchaAPIView(APIView):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        try:
            #获取图片id
            id_ = CaptchaStore.objects.filter(hashkey=hashkey).first().id
            image = captcha_image(request, hashkey)
            #将图片转换为base64
            image_base = base64.b64encode(image.content)
            json_data = json.dumps({"id": id_, "image_base": image_base.decode('utf-8')})
        except:
            json_data = None
        return Response(json_data, content_type="application/json")

class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data=request.data
        email = data.get('email')
        password = data.get('password')
        code = data.get('code')
        try:
            user = User.objects.get(email__exact=email)
            if user and user.password == password:
                serializer = UserSerializer(user)
                self.request.session['user_id'] = user.id
                return Response({'user':serializer.data,'status':status.HTTP_200_OK})
            return Response({'msg':'email or password error','status':status.HTTP_400_BAD_REQUEST})
        except:
            return Response({'msg':'account_not_exist','status':status.HTTP_404_NOT_FOUND})

class UserRegisterAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        email = data.get('email')

        if User.objects.filter(email__exact=email):
            return Response({'msg':"用户邮箱已存在",'status':status.HTTP_400_BAD_REQUEST})
        input_verify = data.get('verify')
        verify_code = request.session['verifycode']
        if input_verify == verify_code:
            serializer = UserRegisterSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                print(serializer.data)
                return Response({'data':serializer.data,'status':status.HTTP_200_OK})
            return Response({'erros':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
        else:
            return Response({'msg':'error with'+verify_code,'status':status.HTTP_400_BAD_REQUEST})

class UserViewSet(viewsets.ModelViewSet,CountModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'email', 'adcode', 'nickname')
    filter_fields = ('id', 'email', 'adcode', 'nickname')

class EmailCodeViewset(viewsets.ModelViewSet,mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    邮箱验证码接口
    """
    queryset = EmailCode.objects.all()
    serializer_class = EmailSerializer

    @action(detail=False, methods=['POST'])
    def test(self,request,*args,**kwargs):
        input_email = request.data.get('email')
        status= send_mail('hello','nihao','tyrantqiao@qq.com',[input_email])
        #email = EmailMessage('hello','nihao',to=['1195502571@qq.com'])
        #email.send()
        return Response('success?')

    @action(detail=False, methods=['POST'])
    def send(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_email = request.data.get('email')
        email = serializer.validate_email(input_email)
        code, email_status = send_register_email(email)
        request.session['verifycode']=''
        if not email_status:
            return Response({'email': "验证发送失败"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            email_record = EmailCode()
            email_record.code = code
            request.session['verifycode'] = code
            email_record.email = email
            email_record.send_type = "register"
            email_record.save()
            print('send here:' + request.session['verifycode'])
            return Response(email_status, status=status.HTTP_201_CREATED)

        self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        return Response({'result':serializer.data}, status=status.HTTP_201_CREATED)
