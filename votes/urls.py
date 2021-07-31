from django.conf.urls import include
from votes.models import RegisteredVoter
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import (
    PartyViewSet,
    CandidateViewSet,
    VoteViewSet,
    VotingEventViewSet,
    RegisteredVoterViewSet
    )


api_router = DefaultRouter()

api_router.register('parties',PartyViewSet)
api_router.register('candidates',CandidateViewSet)
api_router.register('voting/event',VotingEventViewSet)
api_router.register('voting/register',RegisteredVoterViewSet)
api_router.register('voting/vote',VoteViewSet)

urlpatterns = [
    path('',include(api_router.urls)),
]