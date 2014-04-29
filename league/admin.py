from django.contrib import admin

from django.db.models import get_models, get_app


from league.models import *
"""
# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Squad)
"""

#auto register all models in LEAGUE app#
for model in get_models(get_app('league')):
	admin.site.register(model)