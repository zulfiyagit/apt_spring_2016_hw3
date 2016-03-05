"""hw3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from hw3.dictionary.views import *
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'words/en', EnViewSet)
router.register(r'words/ru', RuViewSet)
router.register(r'words/kz', KzViewSet)
router.register(r'words/en/<id>', EnDetailViewSet)
router.register(r'words/ru/<id>', RuDetailViewSet)
router.register(r'words/kz/<id>', KzDetailViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))

]
