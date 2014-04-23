from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

from league.forms import AccountForm


def login(request):
	
	if not request.user.is_authenticated():
		c = {}
		c.update(csrf(request))
		return render(request, 'login.html', c)
	else:
		return HttpResponseRedirect('/')

def auth_view(request):
	#username	= request.POST.get('username', '')
	#password	= request.POST.get('password', '')
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, 
		password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render_to_response('loggedin.html',
		{'name' : request.user.username })

def invalid_login(request):
	if not request.user.is_authenticated():
		return render(request, 'invalid_login.html')
	else:
		return HttpResponseRedirect('/')		

def logout(request):
	auth.logout(request)
	#return render_to_response('logout.html')
	return HttpResponseRedirect('/')


def register_user(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		#form = AccountForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success/')
	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	#args['form'] = AccountForm()
	return render(request, 'register.html', args)

def register_success(request):
	return render(request, 'register_success.html')
