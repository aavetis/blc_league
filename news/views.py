from django.template import RequestContext

from django.shortcuts import render, get_object_or_404
from news.models import *
from forms import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



# Create your views here.
def post(request, post_id):
	post = get_object_or_404(NewsPost, id=post_id)
	context = {
		'post' : post,

	}
	return render(request, 'news_post.html', context, context_instance=RequestContext(request))

def make_post(request):
	if request.user.is_authenticated():
		if request.user.has_perm('news.add_newspost'):
			#show form, user has permission
			if request.POST:
				form = MakePostForm(request.POST)
				if form.is_valid():
					f = form.save(commit=False)
					f.posted_by = request.user
					f.save()

					return HttpResponseRedirect('/')
			else:
				form = MakePostForm()

			args = {}
			args.update(csrf(request))
			args['form'] = form

			return render(request, 'make_post.html', args, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
