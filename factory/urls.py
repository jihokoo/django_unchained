from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<factory_id>[0-9]+)/$', views.show, name='show'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<factory_id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^update$', views.update, name='update'),
]
