from django import forms
from models import *

from django.forms.models import inlineformset_factory


class AccountForm(forms.ModelForm):

	class Meta:
		model = User
		fields = {'username','password',}
				

"""
class TeamForm(forms.ModelForm):
	class Meta:
		model = Squad
		fields = { 'team' }
"""
class TeamForm(forms.ModelForm):
	class Meta:
		model = Squad
		fields = { 'team',  }


	"""
	def save(self, user, *args, **kwargs):
		self.
		self.instance.user = user
		post = super(TeamForm, self).save(*args, **kwargs)
		post.save()
	"""

class MakeTeamForm(forms.ModelForm):
	class Meta:
		model = Team
		
		fields = ('name', 'password', 'bio')

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Player
		exclude = ('user',)
