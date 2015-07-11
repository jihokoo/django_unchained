from django.conf.urls import url

from .controllers import factory

urlpatterns = [
  # api
  url(r'^factory/$', factory.generic, name='factory.generic'),
  url(r'^factory/(?P<factory_id>[0-9]+)/$', factory.detail, name='factory.detail'),
]
