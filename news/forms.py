from django import forms
from models import *


class MakePostForm(forms.ModelForm):
	class Meta:
		model = NewsPost
		
		fields = ('title', 'content',)
