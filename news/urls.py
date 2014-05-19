from django.conf.urls import *

from news import views

urlpatterns = patterns('',


	url(r'^(?P<post_id>\d+)/$', views.news_post, name='news_post'),
    url(r'^make_post/$', views.make_post, name='make_post'),

)