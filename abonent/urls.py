from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from abonent.models import Abonent,Oplata
from abonent.views import abonent_list, person_detail, add_abonent

urlpatterns = [

    url(r'^$',abonent_list, name="abonent_list"),
    url(r'^(?P<person>\d+)', person_detail, name="person"),
    url(r'^add/$', add_abonent, name="add_abonent"),


]
