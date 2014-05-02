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
	
	url(r'^accounts/login/$', 'dja.views.login', name="login"),
    url(r'^accounts/auth/$', 'dja.views.auth_view'),
    url(r'^accounts/logout/$', 'dja.views.logout', name="logout"),
    url(r'^accounts/loggedin/$', 'dja.views.loggedin'),
    url(r'^accounts/invalid/$', 'dja.views.invalid_login'),
    url(r'^accounts/register/$', 'dja.views.register_user', name="register"),
    url(r'^accounts/register_success/$', 'dja.views.register_success'),

    url(r'^accounts/login/$', 'dja.views.login', name="auth_login"),
    url(r'^accounts/register/$', 'dja.views.register_user', name="registration_register"),

    url(r'^user/(?P<u_id>[0-9]+)/$', 'league.views.user', name='user'),
    url(r'^user/edit/$', 'league.views.edit_profile', name="edit_profile"),
    url(r'^user/leave_team/$', 'league.views.leave_team', name="leave_team"),

    url(r'^team/make_team/$', 'league.views.make_team', name="make_team"),
    url(r'^team/join_team/$', 'league.views.join_team', name="join_team"),
    url(r'^team/(?P<t_id>[0-9]+)/$', 'league.views.team_page', name='team_page'),    
    url(r'^team/(?P<t_id>\D+)/$', 'league.views.team_page', name='team_page'),
    

    url(r'^match/(?P<m_id>[0-9]+)/$', 'league.views.match_page', name="match_page"),
    url(r'^match/match_report/$', 'league.views.match_report', name="match_report"),
    

    url(r'^season/(?P<s_id>[0-9]+)/$', 'league.views.season_page', name='season_page'),
    url(r'^join_season/$', 'league.views.join_season', name='join_season'),


    url(r'^forum/', include('pybb.urls', namespace='pybb')),


    url(r'^admin/', include(admin.site.urls)),
)
