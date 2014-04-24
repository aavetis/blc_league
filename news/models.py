from django.db import models
from django.contrib.auth.models import User


class NewsPost(models.Model):
	title = models.CharField(max_length=200)
	posted_by = models.ForeignKey(User)
	content = models.TextField(max_length=600)
	date_posted = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return "%s -- by : %s" %(self.title, self.posted_by.username)