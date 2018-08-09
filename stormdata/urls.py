__author__ = 'Saheed'
__date__ = '08/08/2018'

from django.conf.urls import url
from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.data_analysis, name='data_analysis'),

]