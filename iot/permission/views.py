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
import datetime

# Create your views here.
class UserLoginAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data=request.data
        email = data.get('email')
        password = data.get('password')
        captcha = data.get('captcha')
        user = User.objects.get(email__exact=email)
        if user.password == password:
            serializer = UserSerializer(user)
            self.request.session['user_id'] = user.id
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'code':400,'msg':'email or password error'},status=status.HTTP_400_BAD_REQUEST)

class UserRegisterAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        email = data.get('email')
        if User.objects.filter(email__exact=email):
            return Response("用户邮箱已存在",status.HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet,CountModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'email', 'adcode', 'nickname')
    filter_fields = ('id', 'email', 'adcode', 'nickname')

