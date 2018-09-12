""" Define URL patterns for learning_logs. """

from django.confs.urls import url

from . import views

urlpatterns = [
    #Home Page
    url(r'^$', views.index, name='index'),
]