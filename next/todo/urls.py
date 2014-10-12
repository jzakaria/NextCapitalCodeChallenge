from django.conf.urls import patterns, url
from todo.views import *

urlpatterns = patterns('',
    url(r'^$', register),
    url(r'^([0-9]*)/todos/', todos),
    url(r'^item_mark/', item_mark),
    url(r'^sign_in/', user_login),
    url(r'^sign_out/', user_logout),
    url(r'^/accounts/login$', user_login),
    url(r'^([0-9]*)/archives/', archives),
)