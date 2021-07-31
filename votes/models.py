from django.db import models
from voter.models import Voter

# Create your models here.


class Party(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)


    def __str__(self) -> str:
        return self.name

class Candidate(models.Model):
     name = models.CharField(max_length=50)
     party = models.ForeignKey(Party,null=True,on_delete=models.SET_NULL)
     of_type = models.CharField(max_length=20)


     def __str__(self) -> str:
         return self.name + ' - ' + self.party.name


class VotingEvent(models.Model):
    title = models.CharField(max_length=300)
    date_of_event = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)


class RegisteredVoter(models.Model):
    voting_event = models.ForeignKey(VotingEvent, on_delete=models.CASCADE)
    string = models.CharField(max_length=300)


class Vote(models.Model):
    voting_event = models.ForeignKey(VotingEvent, on_delete=models.CASCADE)
    voter = models.ForeignKey(RegisteredVoter, unique=True, on_delete=models.CASCADE)
    