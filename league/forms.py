from django import forms
from models import *

from django.forms.models import inlineformset_factory


class AccountForm(forms.ModelForm):

	class Meta:
		model = User
		fields = {'username','password',}
				

class TeamForm(forms.ModelForm):
	class Meta:
		model = Squad
		fields = { 'team',  }


class MakeTeamForm(forms.ModelForm):
	class Meta:
		model = Team
		
		fields = ('name', 'password', 'bio')

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = Player
		exclude = ('user',)

class LeaveTeamForm(forms.ModelForm):
	class Meta:
		model = Squad
		fields = ()


class MatchReportForm(forms.ModelForm):
	class Meta:
		model = Match
		fields = (
			'home_score', 'away_score',
		)

class MatchComm(forms.ModelForm):
	class Meta:
		model = MatchMessage
		fields = ('message',)

class JoinSeasonForm(forms.ModelForm):
	class Meta:
		model = Season
		fields = ()



		