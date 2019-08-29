from django.conf.urls import url
from django.urls import path
from spider.views import *

urlpatterns = [
    url(r'^kv/$', kv, name='kv'),
    url(r'^kv/(?P<id>.*)/$', id, name='id'),
]
