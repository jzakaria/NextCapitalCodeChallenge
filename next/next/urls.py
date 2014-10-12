from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo import views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('todo.urls')),
    url(r'^accounts/login/$', views.user_login),
)