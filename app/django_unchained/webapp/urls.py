from django.conf.urls import url

from .controllers import factory

urlpatterns = [
  # web app
  url(r'^factory/$', factory.showAll, name='factory.showAll'),
  url(r'^factory/create$', factory.create, name='factory.create'),
  url(r'^factory/(?P<factory_id>[0-9]+)/$', factory.showOne, name='factory.showOne'),
  url(r'^factory/(?P<factory_id>[0-9]+)/update$', factory.update, name='factory.update'),
  url(r'^factory/(?P<factory_id>[0-9]+)/delete$', factory.delete, name='factory.delete'),
]
