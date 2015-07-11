from django.conf.urls import url

from . import views

urlpatterns = [
  # web app
  url(r'^factory/$', views.showAll, name='showAll'),
  url(r'^factory/create$', views.create, name='create'),
  url(r'^factory/(?P<factory_id>[0-9]+)/$', views.showOne, name='showOne'),
  url(r'^factory/(?P<factory_id>[0-9]+)/update$', views.update, name='update'),
  url(r'^factory/(?P<factory_id>[0-9]+)/delete$', views.delete, name='delete'),
]
