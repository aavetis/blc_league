from django.shortcuts import render, render_to_response, get_object_or_404

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from django.core.context_processors import csrf

from league.models import *
from django.contrib.auth.models import User

from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse



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

    #return render(request, 'home.html', context)
    return render(request, 'home.html', context, context_instance=RequestContext(request))

@login_required
def join_team(request):        
    pl = Player.objects.get(user=request.user)
    if Squad.objects.filter(player=pl):
        return HttpResponseRedirect('/')

    if request.POST:
        form = TeamForm(request.POST)
        if form.is_valid():
            u = request.user
            uid = u.id
            team =Team.objects.get(id=request.POST['team'])
            
            password = request.POST['pw']
            f = form.save(commit=False)
            f.player = pl

            if password == Team.objects.get(id=request.POST['team']).password:
                f.save()
                team.checkPlayers()
                #team.save
            else:
                return HttpResponseRedirect('/')                    
            


            return HttpResponseRedirect('/user/'+str(request.user.id))
    else:
        form = TeamForm()
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(request, 'join_team.html', args, context_instance=RequestContext(request))


@login_required
def make_team(request):
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

    return render(request, 'make_team.html', args, context_instance=RequestContext(request))



def team_page(request, t_id):
    try:
        if Team.objects.get(name__iexact=t_id):
            team = Team.objects.get(name__iexact=t_id)
        elif Team.objects.get(id=t_id):
            team = Team.objects.get(id=t_id)

    except Team.DoesNotExist:
        team = get_object_or_404(Team, id=t_id)

    members = team.members
    


    team_matches = team.home_team.all() | team.away_team.all()
    context = {
        'team' : team,
        'members' : members,
        'team_matches' : team_matches,
    }

    return render(request, 'team.html', context, context_instance=RequestContext(request) )

def user(request, u_id):
    u = User.objects.get(id=u_id)
    pl = Player.objects.get(id=u_id)
    
    context = {
    'u' : u
    }
    
    #check if player has squad
    try:
        s = Squad.objects.get(player=pl)
    except Squad.DoesNotExist:
        s = None
    if s:
        context['team'] = s.team

        user_matches = Match.objects.filter(home=s.team) | Match.objects.filter(away=s.team)
        context['user_matches'] = user_matches
    return render(request, 'profile.html', context, context_instance=RequestContext(request) )

@login_required
def edit_profile(request):
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

    return render(request, 'edit.html', args, context_instance=RequestContext(request))

@login_required
def leave_team(request):
    user = request.user
    pl = Player.objects.get(user=request.user)
    
    squad = get_object_or_404(Squad, player=pl)
    team = squad.team

    if request.POST:
        form = LeaveTeamForm(request.POST, instance=squad)
        if form.is_valid():
            squad.delete()
            team.checkPlayers()
            return HttpResponseRedirect('/')
    else:
        form = LeaveTeamForm(instance=squad)
    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'leave_team.html', args, context_instance=RequestContext(request))


def season_page(request, s_id):
    season = get_object_or_404(Season, id=s_id)
    context = {
        'season' : season
    }

    return render(request, 'season.html', context, context_instance=RequestContext(request))

def match_page(request, m_id):
    current_match = get_object_or_404(Match, id=m_id)
    context = {
        'current_match' : current_match
    }

    context['messages'] = current_match.messages
    #dont show comment form unless loggedin

    context['form'] = MatchComm()
    context.update(csrf(request))
    if request.POST:
        form = MatchComm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.sent_by = request.user
            f.save()

            context['current_match'].messages.add(f)

            return HttpResponseRedirect('/match/'+str(current_match.id)) 


    return render(request, 'match.html', context, context_instance=RequestContext(request))

@login_required
def match_report(request):
    user = request.user
    try:
        team = get_object_or_404(Team, members=user)
        match = team.home_team.filter(status=1) | team.away_team.filter(status=1)
        match = match[0]
    except:
        return HttpResponse("you dont have a match to report")

    if request.POST:
        form = MatchReportForm(request.POST, instance=match)

        if form.is_valid():
            f = form.save(commit=False)
            f.season = Season.objects.get(status='L')
            f.home = match.home
            f.away = match.away
            f.save()
            return HttpResponseRedirect('/match/'+str(match.id)) 
    else:
        form = MatchReportForm(request.POST, instance=match)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['match'] = match
    
    return render(request, 'match_report.html', args, context_instance=RequestContext(request))
    

@login_required
def join_season(request):

    user = request.user
    pl = Player.objects.get(user=request.user)
    try:
        squad = get_object_or_404(Squad, player=pl)
    except:
        return HttpResponseRedirect("/team/join_team/")
        #return HttpResponse("dont have a team to join with")
        #return TemplateResponse(request, 'base.html', "test")
    team = squad.team

    season = get_object_or_404(Season, status='L')

    if team in season.teams.all():
        return HttpResponseRedirect("/season/"+str(season.id))

    if len(team.members.all()) < 3:
        return HttpResponse("not enough players, team not active")

    if request.POST:
        if team.is_active:
            form = JoinSeasonForm(request.POST, instance=season)

            if form.is_valid():                    
                season.teams.add(team)
                form.save()
                season.save()
                #return HttpResponse("joined season")
                return HttpResponseRedirect("/season/"+str(season.id))
        else:
            return HttpResponseRedirect("/")
    else:
        form = JoinSeasonForm(request.POST, instance=season)
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render(request, 'join_season.html', args, context_instance=RequestContext(request))

    






