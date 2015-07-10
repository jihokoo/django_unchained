from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.showAll, name='showAll'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<factory_id>[0-9]+)/$', views.showOne, name='showOne'),
    url(r'^(?P<factory_id>[0-9]+)/update$', views.update, name='update'),
    url(r'^(?P<factory_id>[0-9]+)/delete$', views.delete, name='delete'),
]
