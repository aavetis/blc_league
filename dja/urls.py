from django.conf.urls import patterns, include, url

from django.contrib import admin

from news import urls
from league import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dja.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^news/', include('news.urls')),



    url(r'^$', 'league.views.home', name='home'),

	
	url(r'^accounts/login/$', 'dja.views.login'),
    url(r'^accounts/auth/$', 'dja.views.auth_view'),
    url(r'^accounts/logout/$', 'dja.views.logout'),
    url(r'^accounts/loggedin/$', 'dja.views.loggedin'),
    url(r'^accounts/invalid/$', 'dja.views.invalid_login'),
    
    url(r'^accounts/register/$', 'dja.views.register_user'),
    url(r'^accounts/register_success/$', 'dja.views.register_success'),

    url(r'^user/(?P<u_id>[0-9]+)/$', 'league.views.user', name='user'),
    
    url(r'^user/edit/$', 'league.views.edit_profile'),

    url(r'^team/make_team/$', 'league.views.make_team'),
    url(r'^team/join_team/$', 'league.views.join_team'),
    url(r'^team/(?P<t_id>[0-9]+)/$', 'league.views.team_page', name='team_page'),
    
    url(r'^team/(?P<t_id>\D+)/$', 'league.views.team_page', name='team_page'),
    
    url(r'^user/leave_team/$', 'league.views.leave_team', name="leave_team"),





    url(r'^admin/', include(admin.site.urls)),
)
