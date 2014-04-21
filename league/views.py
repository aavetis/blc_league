from django.shortcuts import render, render_to_response, get_object_or_404

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.core.context_processors import csrf

from league.models import *
from django.contrib.auth.models import User

from django.contrib import auth
from django.http import HttpResponseRedirect

from forms import *


def home(request):
    players = Player.objects.all()
    teams 	= Team.objects.all()
    
    title = "Home"
    context = { 
        'players' : players, 
        'teams' : teams, 
        'title' : title 
    }
    
    #if user is authed, check if hes on a team
    if request.user.is_authenticated():
        p = Player.objects.get(user=request.user)
        if p:
            context['p'] = p

    return render(request, 'home.html', context)


def join_team(request):
    if request.user.is_authenticated():
        
        pl = Player.objects.get(user=request.user)
        if Squad.objects.filter(player=pl):
            return HttpResponseRedirect('/')

        if request.POST:
            form = TeamForm(request.POST)
            if form.is_valid():
                u = request.user
                uid = u.id
                
                password = request.POST['pw']
                f = form.save(commit=False)
                f.player = pl

                if password == Team.objects.get(id=request.POST['team']).password:
                    f.save()
                else:
                    return HttpResponseRedirect('/')                    
                
                return HttpResponseRedirect('/')
        else:
            form = TeamForm()
        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render(request, 'join_team.html', args)
    else:
         return HttpResponseRedirect('/accounts/login/')


def make_team(request):
    if request.user.is_authenticated():
        pl = Player.objects.get(user=request.user)

        if request.POST:
            form = MakeTeamForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = MakeTeamForm()
        args = {}
        args.update(csrf(request))
        args['form'] = form
    
        return render(request, 'make_team.html', args)
    else:
        return HttpResponseRedirect('/accounts/login/')


def team_page(request, t_id):
    team = get_object_or_404(Team, id=t_id)
    members = team.members
    context = {
        'team' : team,
        'members' : members
    }

    return render(request, 'team.html', context )

def user(request, u_id):
    u = User.objects.get(id=u_id)
    pl = Player.objects.get(id=u_id)
    
    context = {
    'u' : u
    }
    s = Squad.objects.get(player=pl)

    if s:
        context['team'] = s.team
    
    return render(request, 'profile.html', context )


def edit_profile(request):
    if request.user.is_authenticated():
        user = request.user
        pl = Player.objects.get(user=request.user)

        if request.POST:
            form = EditProfileForm(request.POST, instance=pl)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = EditProfileForm(instance=pl)
        args = {}
        args.update(csrf(request))
        args['form'] = form
    
        return render(request, 'edit.html', args)
    else:
        return HttpResponseRedirect('/accounts/login/')
    
