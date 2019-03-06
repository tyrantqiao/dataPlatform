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
from api.views import NodesListViewSet,DataListViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# qiao: create rest_framework api 
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# qiao: This register the docs page :8000/docs
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'nodes', NodesListViewSet)
router.register(r'data', DataListViewSet)


# qiao: add rest framwork's login and logout views
# error: django2.0 will not support app_name, change to include('blog.urls')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^', include('api.urls')),
    url(r'^api/', include(router.urls)),
    url(r'docs/', include_docs_urls(title="后台接口")),
    url(r'^', include(router.urls)),
]
