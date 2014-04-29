from news.models import *
from league.models import *


def news_content(request):
	c = {}
	c['newspost'] = NewsPost.objects.all().order_by('-id')[:5]
	return c

def current_season(request):
	c = {}
	c['season'] = Season.objects.get(status="L")
	return c