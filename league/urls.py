from django.conf.urls import patterns, include, url


from . import views


urlpatterns = patterns('',

    url(r'^team/join_team/$', 'league.views.join_team'),



)