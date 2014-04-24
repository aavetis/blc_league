from news.models import *

def news_content(request):
	c = {}
	c['newspost'] = NewsPost.objects.all().order_by('-id')[:5]
	return c