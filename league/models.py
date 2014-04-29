from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.contrib import auth


class Player(models.Model):
    user = models.OneToOneField(User)
    blc_name = models.CharField(blank=False, max_length=30)

    fav_champ = models.CharField(blank=True, max_length=40)
    location = models.CharField(blank=True, max_length=15)
    bio = models.TextField(blank=True, max_length=256)

    def __unicode__(self):
    	return "%s  |  %s" %( self.user.username, self.blc_name)

    def is_on_team(self):
        if Squad.objects.filter(player=self):
            return True
        else:
            return False

    def on_team(self):
        return Squad.objects.get(player=self).team
    """
    class Meta:
        permissions = (
            ('can_')
        )
    """

@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        #give permissions when player created#
        #instance.


class Team(models.Model):
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    bio = models.TextField(max_length=600)
    members = models.ManyToManyField(Player, through='Squad')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.name
    
    def checkPlayers(self):
        n = len(self.members.all())
        if n >= 3:
            self.is_active = True
            self.save()
        elif n < 3:
            self.is_active = False
            self.save()

    def listPlayers(self):
        s = Squad.objects.filter(team = self)
        return s

class Squad(models.Model):
    player = models.ForeignKey(Player)
    team = models.ForeignKey(Team)
    date_joined = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
    	return "%s : %s " %(self.team.name, self.player.user.username)



class Season(models.Model):
    STATUS = (
        ('P', 'Pending'),
        ('L', 'Live'),
        ('C', 'Closed')
    )
    teams  = models.ManyToManyField(Team, related_name="teamlist")
    status = models.CharField(max_length=1, default=STATUS[0][0], choices=STATUS)

    info = models.TextField(blank=True, max_length=2000)

    def __unicode__(self):
        return "Season %d | Status: %s" %(self.id, self.status)

"""
class Match(models.Model):
    STATUS = (
        ('1', 'Pending'),
        ('2', 'HOME WIN'),
        ('3', 'AWAY WIN'),
    )

    home = models.ForeignKey(Team, related_name='home_team')
    home_score = models.PositiveSmallIntegerField(blank=True)
    away = models.ForeignKey(Team, related_name='away_team')
    away_score = models.PositiveSmallIntegerField(blank=True)
    status = models.CharField(max_length=1, default=STATUS[0][0], choices=STATUS)

    messages = models.ManyToManyField(MatchMessage, blank=True)


class MatchMessage(models.Model):
    sent_by = models.ForeignKey(User)
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    match = models.ManyToManyField(Match)


"""