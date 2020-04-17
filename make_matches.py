import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'dja.settings'

from league.models import *
import random
import itertools

teams = Team.objects.filter(is_active=True)
current_season = Season.objects.get(status = 'L')

#
#


l = list(teams)

for TWO_MATCHES_PER_WEEK in range(0,2):	
	print "Week 1.%d" %TWO_MATCHES_PER_WEEK
	random.shuffle(l)
	random.shuffle(l)
	random.shuffle(l)
	print l
	

	for x in xrange(0, len(l), 2):
		try:
			m = Match(season=current_season, home=l[x], away=l[x+1])
		except:
			#random.shuffle(l)
			m = Match(season=current_season, home=l[len(l)-1], away=l[0])
			#pass
		m.save()	
		print m


	print "End Week 1.%d \n\n" %TWO_MATCHES_PER_WEEK
