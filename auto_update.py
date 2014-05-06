import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'dja.settings'

from league.models import *


print "checking matches"
matches = Match.objects.all()

for m in matches:
	print m

print "end list of matches..."

print "check scores of all matches."
for m in matches:
	print m
	print "%s : %d" %(m.home, m.home_score)
	print "%s : %d" %(m.away, m.away_score)
	print "MATCH STATUS: %s" %m.status
	print "***"
	print "***"

	if m.home_score > m.away_score:
		m.status='2'
	elif m.away_score > m.home_score:
		m.status='3'

	print "NEW STATUS: %s" %m.get_status_display()

	m.save()
	print "MATCH UPDATED"