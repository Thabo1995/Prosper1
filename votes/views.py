from django.shortcuts import render
from .models import (
   Vote,
   Voter,
   Party,
   Candidate,
   VotingEvent,
   RegisteredVoter
)

from rest_framework import viewsets , serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from .serializers import PartySerializer,VoteSerializer,CandidateSerializer



class PartyViewSet(viewsets.ModelViewSet):
    """
    A view that returns the political parties in JSON.
    """
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['get']



class CandidateViewSet(viewsets.ModelViewSet):
    """
    A view that returns the candidates in JSON.
    """
    
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['get']



class VoteViewSet(viewsets.ModelViewSet):
    """
    A view for voting
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['post']


class RegisteredVoterViewSet(viewsets.ModelViewSet):
    """
    A view for voting
    """
    
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['post']



class VotingEventViewSet(viewsets.ModelViewSet):
    """
    A view for latest voting event.
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    filter_backends = (DjangoFilterBackend,)
    http_method_names = ['get']
    
