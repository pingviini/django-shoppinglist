from django.conf.urls import patterns, url
from shoppinglist import views


urlpatterns = patterns(
    '',
    url(r'^/add/$', views.add),
)
