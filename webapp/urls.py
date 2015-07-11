from django.conf.urls import url

from . import views

urlpatterns = [
  # web app
  url(r'^factory/$', views.showAll, name='factory.showAll'),
  url(r'^factory/create$', views.create, name='factory.create'),
  url(r'^factory/(?P<factory_id>[0-9]+)/$', views.showOne, name='factory.showOne'),
  url(r'^factory/(?P<factory_id>[0-9]+)/update$', views.update, name='factory.update'),
  url(r'^factory/(?P<factory_id>[0-9]+)/delete$', views.delete, name='factory.delete'),
]
