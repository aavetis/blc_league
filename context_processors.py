from news.models import *
from league.models import *
from pybb.models import *

from pybb.views import *


def news_content(request):
	c = {}
	c['newspost'] = NewsPost.objects.all().order_by('-id')[:5]

	#c['forumposts'] = Post.objects.order_by('-created')[:10]
	c['forumposts'] = Topic.objects.order_by('-updated')[:10]
	return c

def current_season(request):
	c = {}
	c['season'] = Season.objects.get(status="L")
	c['season_sorted'] = c['season'].matches.all().order_by('-id')[:5]
	return c

def match_info(request):
	c = {}

	try:
		team = Team.objects.get(members=request.user)
		c['match'] = team.home_team.filter(status=1) | team.away_team.filter(status=1)
		c['match'] = c['match'][0]
		#c['matchmessages'] = c['match'].messages
	except:
		pass

	return c
