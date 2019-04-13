"""iot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# qiao: apis for frontend
from api.views import NodesListViewSet,DataListViewSet,SearchDataListViewSet,OrderListViewSet,CommodityListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from permission.views import *

# Routers provide an easy way of automatically determining the URL conf.
# qiao: This register the docs page :8000/docs
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'nodes', NodesListViewSet)
router.register(r'data', DataListViewSet)
router.register(r'searchData', SearchDataListViewSet)
router.register(r'order', OrderListViewSet)
router.register(r'commodity', CommodityListViewSet)
router.register(r'user', UserViewSet)
router.register(r'email', EmailCodeViewset)

# qiao: add rest framwork's login and logout views
# error: django2.0 will not support app_name, change to include('blog.urls')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^', include('api.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^register/', UserRegisterAPIView.as_view()),
    url(r'^login/', UserLoginAPIView.as_view()),
    url(r'^vertification/', CaptchaAPIView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^permission/', include(router.urls)),
    url(r'docs/', include_docs_urls(title="后台接口")),
    url(r'^', include(router.urls)),
]
