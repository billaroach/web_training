from django.contrib import admin
from django.urls import path
from Beer import views
from Beer.models import Beer
from django.conf.urls import url
from django.views.generic import ListView, DetailView


urlpatterns =[

    url(r'^$', views.index, name='index'),
    url(r'^all_beer/$', views.all_beer, name='all_beer'),
    url(r'^black_beer/$', views.black_beer, name='black_beer'),
    url(r'^light_beer/$', views.light_beer, name='light_beer'),
    url(r'^all_beer/(?P<pk>\d+)$', views.details_beer, name='details_beer'),
    url(r'^add_comment/(?P<pk>\d+)$', views.add_comment, name='add_comment'),
    url(r'^add_beer/$', views.add_beer, name='add_beer'),


]

